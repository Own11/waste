from django.core.management.base import BaseCommand
from api.models import User, Outlet
# pyrefly: ignore [missing-import]
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Seeds database with initial outlets, senders, and checkers'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # 1. Create Outlets
        outlets_data = [
            {"name": "Центральная Кофейня", "address": "ул. Ленина, 12"},
            {"name": "Булочная на Углу", "address": "пр. Мира, 45"},
            {"name": "Пиццерия Mentoria", "address": "ул. Пушкина, 7"}
        ]
        
        for data in outlets_data:
            outlet, created = Outlet.objects.get_or_create(
                name=data["name"],
                defaults={"address": data["address"]}
            )
            if created:
                self.stdout.write(f"Created outlet: {outlet.name}")

        # 2. Create Senders (employees)
        senders_data = [
            {"username": "sender1", "password": "sender123", "first_name": "Иван", "last_name": "Иванов"},
            {"username": "sender2", "password": "sender123", "first_name": "Петр", "last_name": "Петров"}
        ]
        for data in senders_data:
            user, created = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "role": "sender"
                }
            )
            if created:
                user.set_password(data["password"])
                user.save()
                Token.objects.get_or_create(user=user)
                self.stdout.write(f"Created sender user: {user.username}")

        # 3. Create Checker (reviewer)
        checker, created = User.objects.get_or_create(
            username="checker1",
            defaults={
                "first_name": "Анна",
                "last_name": "Смирнова",
                "role": "checker"
            }
        )
        if created:
            checker.set_password("checker123")
            checker.save()
            Token.objects.get_or_create(user=checker)
            self.stdout.write(f"Created checker user: {checker.username}")

        # 4. Create Admin / Superuser
        admin, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "first_name": "Администратор",
                "last_name": "Системы",
                "role": "checker",
                "is_staff": True,
                "is_superuser": True
            }
        )
        if created:
            admin.set_password("admin123")
            admin.save()
            Token.objects.get_or_create(user=admin)
            self.stdout.write(f"Created admin user: {admin.username}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
