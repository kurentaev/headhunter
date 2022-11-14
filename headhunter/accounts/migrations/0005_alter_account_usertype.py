# Generated by Django 4.1.3 on 2022-11-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='usertype',
            field=models.CharField(choices=[('company', 'Компания'), ('candidate', 'Кандидат')], max_length=250, verbose_name='Пользователь'),
        ),
    ]
