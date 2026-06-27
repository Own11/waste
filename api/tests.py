from django.urls import reverse
# pyrefly: ignore [missing-import]
from rest_framework.test import APITestCase
# pyrefly: ignore [missing-import]
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import User, Outlet, WriteOffRequest
from api.services import IikoService

class WriteOffSystemTests(APITestCase):
    def setUp(self):
        # Create users with different roles
        self.sender = User.objects.create_user(
            username='sender_test', password='password123', role='sender',
            first_name='Ivan', last_name='Ivanov'
        )
        self.checker = User.objects.create_user(
            username='checker_test', password='password123', role='checker',
            first_name='Anna', last_name='Smirnova'
        )
        
        # Create an outlet
        self.outlet = Outlet.objects.create(
            name="Тестовая Точка",
            address="ул. Тестовая, 1"
        )
        
        # URL constants
        self.token_url = reverse('token_obtain')
        self.outlet_list_url = reverse('outlet-list')
        self.write_off_list_url = reverse('writeoff-list')
        self.request_list_url = reverse('request-list')

        # Dummy image for upload
        self.dummy_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )

    def test_token_obtain_returns_role(self):
        """Verify that login endpoint returns the token and the user role."""
        response = self.client.post(self.token_url, {
            'username': 'sender_test',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['role'], 'sender')
        self.assertEqual(response.data['username'], 'sender_test')

    def test_outlet_list_accessible_by_authenticated(self):
        """Verify outlets list is accessible by authenticated users."""
        # Unauthenticated request
        response = self.client.get(self.outlet_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Authenticated request
        self.client.force_authenticate(user=self.sender)
        response = self.client.get(self.outlet_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Тестовая Точка")

    def test_write_off_request_validation(self):
        """Verify model validation constraints (min comment length, responsible user requirement)."""
        self.client.force_authenticate(user=self.sender)
        
        # 1. Comment length too short (<10 chars)
        response = self.client.post(self.write_off_list_url, {
            'outlet': self.outlet.id,
            'photo': self.dummy_image,
            'type': 'no_deduction',
            'comment': 'Short'
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('comment', response.data)

        # Reset photo file pointer
        self.dummy_image.seek(0)

        # 2. Withholding type but no responsible user
        response = self.client.post(self.write_off_list_url, {
            'outlet': self.outlet.id,
            'photo': self.dummy_image,
            'type': 'with_deduction',
            'comment': 'Valid comment of appropriate length'
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('responsible_user', response.data)

    def test_create_write_off_request_success(self):
        """Verify that a sender can create a write-off request successfully."""
        self.client.force_authenticate(user=self.sender)
        
        response = self.client.post(self.write_off_list_url, {
            'outlet': self.outlet.id,
            'photo': self.dummy_image,
            'type': 'no_deduction',
            'comment': 'This comment is long enough.'
        }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'on_review')
        self.assertEqual(response.data['author']['username'], 'sender_test')

    def test_review_permission_checks(self):
        """Verify that only users with checker role can view and review requests."""
        # Create a request
        request = WriteOffRequest.objects.create(
            outlet=self.outlet,
            author=self.sender,
            photo=self.dummy_image,
            type='no_deduction',
            comment='This comment is long enough.',
            status='on_review'
        )

        review_url = reverse('request-review', args=[request.id])

        # Sender tries to view reviewer endpoint
        self.client.force_authenticate(user=self.sender)
        response = self.client.get(self.request_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Sender tries to review request
        response = self.client.post(review_url, {'action': 'approve'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Checker gets reviewer list
        self.client.force_authenticate(user=self.checker)
        response = self.client.get(self.request_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_review_approve_integration_success(self):
        """Verify that approving a request calls IikoService and changes status to written off."""
        request = WriteOffRequest.objects.create(
            outlet=self.outlet,
            author=self.sender,
            photo=self.dummy_image,
            type='no_deduction',
            comment='Valid comment for testing iiko sync.',
            status='on_review'
        )

        self.client.force_authenticate(user=self.checker)
        review_url = reverse('request-review', args=[request.id])
        
        response = self.client.post(review_url, {'action': 'approve'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify status is updated to 'iiko_synced' and act ID is saved
        self.assertEqual(response.data['status'], 'iiko_synced')
        self.assertIsNotNone(response.data['iiko_act_id'])
        self.assertTrue(response.data['iiko_act_id'].startswith('iiko-act-'))

    def test_review_reject(self):
        """Verify that rejecting a request updates status to rejected."""
        request = WriteOffRequest.objects.create(
            outlet=self.outlet,
            author=self.sender,
            photo=self.dummy_image,
            type='no_deduction',
            comment='Valid comment for testing rejection.',
            status='on_review'
        )

        self.client.force_authenticate(user=self.checker)
        review_url = reverse('request-review', args=[request.id])
        
        response = self.client.post(review_url, {'action': 'reject'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'rejected')
        self.assertIsNone(response.data['iiko_act_id'])

    def test_index_page_loads(self):
        """Verify that the home page (root URL) serves index.html and loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "<title>Bahandi Write-Offs</title>")

