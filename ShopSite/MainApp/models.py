from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='User-email')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user_photo = models.ImageField()
    STATUS_CHOICES = [
        ('доставщик', 'Доставщик'),
        ('продавец', 'Продавец'),
        ('пользователь', 'Пользователь'),
    ]
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='пользователь', blank=True, null=True)

    def __str__(self):
        return self.username


class Announcement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    descriptions = models.TextField()

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('в ожидании', 'В ожидании'),
        ('отправлено', 'Отправлено'),
        ('доставлено', 'Доставлено'),
        ('отменено', 'Отменено'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='в ожидании')
    salesman = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sales_orders', on_delete=models.CASCADE)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='provider_orders', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_orders', on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='announcement')

    def __str__(self) -> str:
        return f'Доставщик: {self.salesman} - Продавец: {self.provider} - Пользователь: {self.user} - Объевление: {self.announcement}'
