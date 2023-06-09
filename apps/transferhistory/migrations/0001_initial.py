# Generated by Django 4.1.7 on 2023-03-18 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('amount', models.IntegerField(verbose_name='Сумма перевода')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_user', to=settings.AUTH_USER_MODEL, verbose_name='От какого пользователя')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Кому')),
            ],
            options={
                'verbose_name': 'Перевод',
                'verbose_name_plural': 'Переводы',
            },
        ),
    ]
