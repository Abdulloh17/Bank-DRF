# Generated by Django 4.1.7 on 2023-03-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_users', '0002_alter_user_wallet_adress_historytransfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet_adress',
            field=models.CharField(default='e260192b04d2', max_length=12, unique=True, verbose_name='Номер кошелька'),
        ),
        migrations.DeleteModel(
            name='HistoryTransfer',
        ),
    ]