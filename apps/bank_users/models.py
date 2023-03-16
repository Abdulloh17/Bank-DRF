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


class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
         User,
         on_delete=models.CASCADE,
         verbose_name='От какого пользователя',
         related_name='transfer_user',
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кому',
        related_name='receiver',
    )
    is_completed = models.BooleanField(
        verbose_name='Статус',
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    amount = models.IntegerField(
        verbose_name='Сумма перевода',
    )

    def __str__(self) -> str:
        return f'От {self.from_user} кому {self.to_user}'
    
    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
