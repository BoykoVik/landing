# Generated by Django 4.0.4 on 2022-05-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0004_alter_calculate_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='titlealt',
            field=models.TextField(blank=True, max_length=350, verbose_name='для тега alt'),
        ),
        migrations.AddField(
            model_name='works',
            name='titlealt',
            field=models.TextField(blank=True, max_length=350, verbose_name='для тега alt'),
        ),
    ]