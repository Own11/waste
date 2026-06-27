from django.contrib.auth.models import AbstractUser
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    city = models.CharField(max_length=100, verbose_name="Город")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return f"{self.name} ({self.city})"


class User(AbstractUser):
    ROLE_CHOICES = (
        ('worker', 'Работник (Worker)'),
        ('manager', 'Менеджер (Manager)'),
        ('admin', 'Администратор (Admin)'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='worker')
    fullname = models.CharField(max_length=255, verbose_name="ФИО", blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, related_name='users', verbose_name="Филиал")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Product(models.Model):
    TYPE_CHOICES = (
        ('piece', 'Штучный'),
        ('weight', 'Весовой'),
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    sku = models.CharField(max_length=100, unique=True, verbose_name="Артикул/Штрихкод")
    unit_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='piece', verbose_name="Тип товара")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    contacts = models.TextField(verbose_name="Контакты")
    ai_rating = models.FloatField(default=5.0, verbose_name="Текущий AI-рейтинг")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplies', verbose_name="Поставщик")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='supplies', verbose_name="Филиал")
    date = models.DateTimeField(verbose_name="Дата поставки")
    photos = models.JSONField(default=list, verbose_name="Фотографии поставки", blank=True)
    ai_status_report = models.JSONField(default=dict, verbose_name="AI Status Report", blank=True)

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"

    def __str__(self):
        return f"Поставка #{self.id} от {self.supplier.name}"


class WriteOff(models.Model):
    REASON_CHOICES = (
        ('expiration', 'Просрочка'),
        ('spoiled', 'Испорчен'),
        ('damaged', 'Поврежден'),
        ('cooking_error', 'Ошибка приготовления'),
        ('supplier_defect', 'Брак поставщика'),
        ('other', 'Другое'),
    )
    STATUS_CHOICES = (
        ('pending', 'На проверке (Pending)'),
        ('approved', 'Одобрено (Approved)'),
        ('rejected', 'Отклонено (Rejected)'),
    )

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='write_offs', verbose_name="Сотрудник")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='write_offs', verbose_name="Филиал")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='write_offs', verbose_name="Товар")
    photo = models.ImageField(upload_to='write_offs/', verbose_name="Фотография списания", null=True, blank=True)
    ai_confidence = models.FloatField(default=0.0, verbose_name="Вероятность распознавания AI")
    reason = models.CharField(max_length=20, choices=REASON_CHOICES, verbose_name="Причина")
    quantity = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Количество")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_write_offs', verbose_name="Менеджер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обработки")

    class Meta:
        verbose_name = "Списание"
        verbose_name_plural = "Списания"
        ordering = ['-created_at']

    def __str__(self):
        return f"Списание #{self.id} - {self.product.name} ({self.get_status_display()})"


class EmployeeBadge(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges', verbose_name="Сотрудник")
    badge_name = models.CharField(max_length=255, verbose_name="Название бейджа")
    date_received = models.DateField(auto_now_add=True, verbose_name="Дата получения")

    class Meta:
        verbose_name = "Бейдж сотрудника"
        verbose_name_plural = "Бейджи сотрудников"

    def __str__(self):
        return f"{self.employee.username} - {self.badge_name}"
