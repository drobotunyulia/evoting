# Generated by Django 4.2.13 on 2024-05-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='finish_date',
            field=models.DateField(verbose_name='Конец голосования'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_date',
            field=models.DateField(verbose_name='Начало голосования'),
        ),
    ]
