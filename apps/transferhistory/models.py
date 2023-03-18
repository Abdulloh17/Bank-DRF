from django.db import models

from apps.bank_users.models import User
# Create your models here.

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
