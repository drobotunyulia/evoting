# Generated by Django 4.2.13 on 2024-05-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_validator_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='result',
            field=models.IntegerField(default=0, null=True, verbose_name='Результат'),
        ),
    ]