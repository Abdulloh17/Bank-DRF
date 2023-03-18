from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Ваша почта',
        unique=True,
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Ваш тел. номер',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    age = models.CharField(
        max_length=2,
        verbose_name='Ваш возраст',
    )
    wallet_adress = models.CharField(
        max_length=12,
        unique=True,
        default=uuid.uuid4().hex[:12],
        verbose_name='Номер кошелька',
    )
    balance = models.IntegerField(
        verbose_name='Баланс',
        default=0,
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


