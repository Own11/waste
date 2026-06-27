from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import User, Branch, Product, Supplier, Supply, WriteOff, EmployeeBadge
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds database with branches, products, suppliers, workers, managers, and badges'

    def handle(self, *args, **options):
        self.stdout.write('Seeding expanded database...')

        # 1. Create Branches
        branches_data = [
            {"name": "Центральный Филиал", "city": "Астана", "latitude": 51.169392, "longitude": 71.449074},
            {"name": "Филиал Алматы-1", "city": "Алматы", "latitude": 43.238949, "longitude": 76.889709},
            {"name": "Бутик Mentoria", "city": "Караганда", "latitude": 49.801878, "longitude": 73.102142}
        ]
        
        branches = []
        for data in branches_data:
            branch, created = Branch.objects.get_or_create(
                name=data["name"],
                defaults={
                    "city": data["city"],
                    "latitude": data["latitude"],
                    "longitude": data["longitude"]
                }
            )
            branches.append(branch)
            if created:
                self.stdout.write(f"Created branch: {branch.name}")

        # 2. Create Products
        products_data = [
            {"name": "Куриная котлета", "sku": "PRD-CHICK-CUT", "unit_type": "piece", "unit_price": Decimal("450.00")},
            {"name": "Томаты свежие", "sku": "PRD-TOMATO", "unit_type": "weight", "unit_price": Decimal("1200.00")},
            {"name": "Булочка для бургера", "sku": "PRD-BURGER-BUN", "unit_type": "piece", "unit_price": Decimal("150.00")},
            {"name": "Молоко коровье 3.2%", "sku": "PRD-MILK", "unit_type": "weight", "unit_price": Decimal("650.00")}
        ]
        
        products = []
        for data in products_data:
            product, created = Product.objects.get_or_create(
                sku=data["sku"],
                defaults={
                    "name": data["name"],
                    "unit_type": data["unit_type"],
                    "unit_price": data["unit_price"]
                }
            )
            products.append(product)
            if created:
                self.stdout.write(f"Created product: {product.name}")

        # 3. Create Suppliers
        suppliers_data = [
            {"name": "FreshFood", "contacts": "fresh@food.kz, +7701223344", "ai_rating": 4.8},
            {"name": "AgroLine", "contacts": "sales@agroline.kz, +7705556677", "ai_rating": 4.5},
            {"name": "Baker Pro", "contacts": "info@bakerpro.kz, +7702888990", "ai_rating": 4.9},
            {"name": "Qazaq Dairy", "contacts": "milk@qazaqdairy.kz, +7707333221", "ai_rating": 4.2}
        ]
        
        suppliers = []
        for data in suppliers_data:
            supplier, created = Supplier.objects.get_or_create(
                name=data["name"],
                defaults={
                    "contacts": data["contacts"],
                    "ai_rating": data["ai_rating"]
                }
            )
            suppliers.append(supplier)
            if created:
                self.stdout.write(f"Created supplier: {supplier.name}")

        # 4. Create Users (Workers, Managers, Admins)
        # Workers
        workers_info = [
            {"username": "worker1", "password": "worker123", "fullname": "Иван Иванов", "branch": branches[0]},
            {"username": "worker2", "password": "worker123", "fullname": "Петр Петров", "branch": branches[1]}
        ]
        workers = []
        for info in workers_info:
            user, created = User.objects.get_or_create(
                username=info["username"],
                defaults={
                    "fullname": info["fullname"],
                    "role": "worker",
                    "branch": info["branch"]
                }
            )
            if created:
                user.set_password(info["password"])
                user.save()
                self.stdout.write(f"Created worker user: {user.username}")
            workers.append(user)

        # Manager
        manager, created = User.objects.get_or_create(
            username="manager1",
            defaults={
                "fullname": "Анна Смирнова",
                "role": "manager",
                "branch": branches[0]
            }
        )
        if created:
            manager.set_password("manager123")
            manager.save()
            self.stdout.write(f"Created manager user: {manager.username}")

        # Admin
        admin, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "fullname": "Администратор Системы",
                "role": "admin"
            }
        )
        if created:
            admin.set_password("admin123")
            admin.save()
            self.stdout.write(f"Created admin user: {admin.username}")

        # 5. Create Badges
        badges_data = [
            {"employee": workers[0], "badge_name": "Самая аккуратная работа"},
            {"employee": workers[0], "badge_name": "Лучший сотрудник месяца"},
            {"employee": workers[1], "badge_name": "Минимум потерь"}
        ]
        for data in badges_data:
            badge, created = EmployeeBadge.objects.get_or_create(
                employee=data["employee"],
                badge_name=data["badge_name"]
            )
            if created:
                self.stdout.write(f"Awarded badge '{badge.badge_name}' to {badge.employee.username}")

        # 6. Create initial WriteOffs for analytics population
        writeoffs_data = [
            {
                "employee": workers[0],
                "branch": branches[0],
                "product": products[0], # chicken cutlet
                "ai_confidence": 94.2,
                "reason": "cooking_error",
                "quantity": Decimal("10.000"),
                "status": "approved",
                "manager": manager
            },
            {
                "employee": workers[0],
                "branch": branches[0],
                "product": products[1], # tomato
                "ai_confidence": 88.5,
                "reason": "expiration",
                "quantity": Decimal("25.500"),
                "status": "approved",
                "manager": manager
            },
            {
                "employee": workers[1],
                "branch": branches[1],
                "product": products[3], # milk
                "ai_confidence": 91.0,
                "reason": "supplier_defect",
                "quantity": Decimal("40.000"),
                "status": "approved",
                "manager": manager
            },
            {
                "employee": workers[0],
                "branch": branches[0],
                "product": products[2], # bun
                "ai_confidence": 93.4,
                "reason": "spoiled",
                "quantity": Decimal("15.000"),
                "status": "pending",
                "manager": None
            }
        ]
        
        for data in writeoffs_data:
            wo, created = WriteOff.objects.get_or_create(
                employee=data["employee"],
                branch=data["branch"],
                product=data["product"],
                reason=data["reason"],
                quantity=data["quantity"],
                defaults={
                    "ai_confidence": data["ai_confidence"],
                    "status": data["status"],
                    "manager": data["manager"]
                }
            )
            if created:
                self.stdout.write(f"Created write-off log: Product {wo.product.name} (status: {wo.status})")

        # 7. Create mock supplies with reports
        supplies_data = [
            {
                "supplier": suppliers[0],
                "branch": branches[0],
                "date": timezone.now() - timezone.timedelta(days=2),
                "photos": ["delivery_fresh1.jpg"],
                "ai_status_report": {
                    "defect_rate_percent": 3.2,
                    "freshness_score": 96.5,
                    "packaging_status": "OK",
                    "ai_evaluation": "Поставка в отличном состоянии. Брак в пределах нормы."
                }
            },
            {
                "supplier": suppliers[1],
                "branch": branches[1],
                "date": timezone.now() - timezone.timedelta(days=1),
                "photos": ["delivery_agro1.jpg"],
                "ai_status_report": {
                    "defect_rate_percent": 8.5,
                    "freshness_score": 89.0,
                    "packaging_status": "Damaged Box",
                    "ai_evaluation": "Зафиксировано превышение нормы брака (8.5%). Повреждена внешняя упаковка."
                }
            }
        ]
        for data in supplies_data:
            supply, created = Supply.objects.get_or_create(
                supplier=data["supplier"],
                branch=data["branch"],
                date=data["date"],
                defaults={
                    "photos": data["photos"],
                    "ai_status_report": data["ai_status_report"]
                }
            )
            if created:
                self.stdout.write(f"Logged supply from {supply.supplier.name} with AI report.")

        self.stdout.write(self.style.SUCCESS('Successfully seeded expanded database!'))
