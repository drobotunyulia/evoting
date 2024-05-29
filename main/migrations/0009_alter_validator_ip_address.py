# Generated by Django 4.2.13 on 2024-05-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_validator_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validator',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0', null=True),
        ),
    ]