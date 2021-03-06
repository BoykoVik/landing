# Generated by Django 4.0.4 on 2022-05-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование услуги')),
                ('about', models.CharField(max_length=250, verbose_name='О услуге')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Servicesdop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование услуги')),
                ('about', models.CharField(max_length=250, verbose_name='О услуге')),
            ],
            options={
                'verbose_name': 'Доп услуга',
                'verbose_name_plural': 'Доп услуги',
                'ordering': ['-id'],
            },
        ),
    ]
