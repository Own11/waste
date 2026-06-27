from django.urls import reverse
# pyrefly: ignore [missing-import]
from rest_framework.test import APITestCase
# pyrefly: ignore [missing-import]
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from api.models import User, Branch, Product, Supplier, Supply, WriteOff, EmployeeBadge
from decimal import Decimal

class ExpandedWriteOffSystemTests(APITestCase):
    def setUp(self):
        # 1. Create Branches
        self.branch_astana = Branch.objects.create(
            name="Астана Сити", city="Астана", latitude=51.16, longitude=71.44
        )
        self.branch_almaty = Branch.objects.create(
            name="Алматы Хаб", city="Алматы", latitude=43.23, longitude=76.88
        )

        # 2. Create Users
        self.worker = User.objects.create_user(
            username='worker_test', password='password123', role='worker',
            fullname='Иван Работников', branch=self.branch_astana
        )
        self.manager = User.objects.create_user(
            username='manager_test', password='password123', role='manager',
            fullname='Анна Менеджерова', branch=self.branch_astana
        )
        self.admin = User.objects.create_user(
            username='admin_test', password='password123', role='admin',
            fullname='Алексей Админов'
        )

        # 3. Create Products
        self.cutlet = Product.objects.create(
            name="Куриная котлета", sku="PRD-CHICK-CUT", unit_type="piece", unit_price=Decimal("450.00")
        )
        self.tomato = Product.objects.create(
            name="Томаты свежие", sku="PRD-TOMATO", unit_type="weight", unit_price=Decimal("1200.00")
        )

        # 4. Create Suppliers
        self.supplier = Supplier.objects.create(
            name="FreshFood", contacts="fresh@food.kz, +7701223344", ai_rating=5.0
        )

        # Dummy Image for API uploads
        self.dummy_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )

    def get_jwt_token(self, username, password):
        login_url = reverse('token_obtain')
        response = self.client.post(login_url, {'username': username, 'password': password})
        return response.data['access']

    # --- AUTHENTICATION & SECURITY TESTS ---

    def test_jwt_auth_login_returns_role(self):
        login_url = reverse('token_obtain')
        response = self.client.post(login_url, {
            'username': 'worker_test',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertEqual(response.data['role'], 'worker')
        self.assertEqual(response.data['fullname'], 'Иван Работников')

    def test_worker_endpoints_restrict_unauthorized(self):
        profile_url = reverse('worker_profile')
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_worker_endpoints_restrict_managers(self):
        profile_url = reverse('worker_profile')
        token = self.get_jwt_token('manager_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- WORKER BUSINESS TESTS ---

    def test_worker_profile_retrieval(self):
        # Add a badge and a mock write-off
        EmployeeBadge.objects.create(employee=self.worker, badge_name="Самая аккуратная работа")
        WriteOff.objects.create(
            employee=self.worker, branch=self.branch_astana, product=self.cutlet,
            reason="cooking_error", quantity=Decimal("5.0"), status="approved", manager=self.manager
        )

        profile_url = reverse('worker_profile')
        token = self.get_jwt_token('worker_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('ai_recommendations', response.data)
        self.assertEqual(len(response.data['badges']), 1)
        self.assertEqual(response.data['badges'][0]['badge_name'], "Самая аккуратная работа")
        self.assertEqual(response.data['statistics']['total_write_offs'], 1)
        self.assertIn("таймер", response.data['ai_recommendations']) # Matches specific cooking error tip logic

    def test_worker_write_off_scan(self):
        scan_url = reverse('worker_write_off_scan')
        token = self.get_jwt_token('worker_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        response = self.client.post(scan_url, {'photo': self.dummy_image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['product_name'], "Куриная котлета")
        self.assertEqual(response.data['confidence'], 93.4)

    def test_worker_write_off_create(self):
        create_url = reverse('worker_write_off_create')
        token = self.get_jwt_token('worker_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        self.dummy_image.seek(0)
        response = self.client.post(create_url, {
            'product': self.tomato.id,
            'quantity': '2.500',
            'reason': 'spoiled',
            'photo': self.dummy_image
        }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'pending')
        self.assertEqual(float(response.data['quantity']), 2.5)

    # --- MANAGER & REVIEW TESTS ---

    def test_manager_review_write_off_approve(self):
        write_off = WriteOff.objects.create(
            employee=self.worker, branch=self.branch_astana, product=self.cutlet,
            reason="expiration", quantity=Decimal("12.0"), status="pending"
        )
        
        review_url = reverse('manager_review', args=[write_off.id])
        token = self.get_jwt_token('manager_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        response = self.client.patch(review_url, {'action': 'approve'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'approved')
        self.assertEqual(response.data['manager'], self.manager.id)

    def test_manager_supply_quality_check(self):
        check_url = reverse('manager_supply_check')
        token = self.get_jwt_token('manager_test', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        self.dummy_image.seek(0)
        response = self.client.post(check_url, {
            'supplier': self.supplier.id,
            'branch': self.branch_astana.id,
            'date': timezone.now().isoformat(),
            'photo': self.dummy_image
        }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('ai_analysis', response.data)
        self.assertIn('defect_rate_percent', response.data['ai_analysis'])
        # Assert rating recalculation triggered
        self.assertNotEqual(Supplier.objects.get(pk=self.supplier.id).ai_rating, 5.0)

    # --- EXECUTIVE ANALYTICS TESTS ---

    def test_executive_analytics_dashboard_metrics(self):
        # Create approved losses to aggregate
        WriteOff.objects.create(
            employee=self.worker, branch=self.branch_astana, product=self.cutlet,
            reason="expiration", quantity=Decimal("10.0"), status="approved", manager=self.manager
        )
        WriteOff.objects.create(
            employee=self.worker, branch=self.branch_almaty, product=self.tomato,
            reason="supplier_defect", quantity=Decimal("5.0"), status="approved", manager=self.manager
        )

        dashboard_url = reverse('analytics_dashboard')
        token = self.get_jwt_token('manager_test', 'password123') # Manager behaves as Executive
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        response = self.client.get(dashboard_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 10 cutlets * 450 = 4500. 5 tomatoes * 1200 = 6000. Total = 10500 ₸.
        self.assertEqual(response.data['total_losses_tenge'], 10500.0)
        self.assertEqual(len(response.data['losses_by_branch']), 2) # Astana, Almaty
        self.assertTrue(response.data['prevented_losses_tenge'] > 0)
        self.assertIn('ai_daily_insight', response.data)
