from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class User(AbstractUser):
    ROLE_CHOICES = (
        ('sender', 'Сотрудник (Sender)'),
        ('checker', 'Проверяющий (Checker)'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='sender')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Outlet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    address = models.CharField(max_length=500, verbose_name="Адрес")

    class Meta:
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return self.name


class WriteOffRequest(models.Model):
    TYPE_CHOICES = (
        ('no_deduction', 'Без удержания'),
        ('with_deduction', 'С удержанием'),
    )
    STATUS_CHOICES = (
        ('on_review', 'На проверке'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
        ('iiko_synced', 'Списано в iiko'),
    )

    outlet = models.ForeignKey(
        Outlet, 
        on_delete=models.CASCADE, 
        related_name='write_offs', 
        verbose_name="Торговая точка"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='created_requests', 
        verbose_name="Автор"
    )
    photo = models.ImageField(
        upload_to='write_offs/', 
        verbose_name="Фото списания"
    )
    type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='no_deduction', 
        verbose_name="Тип списания"
    )
    responsible_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='responsible_requests', 
        verbose_name="Сотрудник для удержания"
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        validators=[MinLengthValidator(10, message="Комментарий должен содержать не менее 10 символов.")]
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='on_review', 
        verbose_name="Статус"
    )
    iiko_act_id = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        verbose_name="ID акта iiko"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Заявка на списание"
        verbose_name_plural = "Заявки на списание"
        ordering = ['-created_at']

    def clean(self):
        super().clean()
        if self.comment and len(self.comment) < 10:
            raise ValidationError({'comment': "Комментарий должен содержать не менее 10 символов."})
        if self.type == 'with_deduction' and not self.responsible_user:
            raise ValidationError({'responsible_user': "Для списания с удержанием необходимо указать сотрудника."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заявка #{self.id} - {self.outlet.name} - {self.get_status_display()}"
