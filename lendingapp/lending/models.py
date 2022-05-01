from django.db import models

# Create your models here.

CHOICES = [
    ('1', 'Сайт'),
    ('2', 'Дизайн'),
    ]

class Services(models.Model):
    title = models.CharField(blank=False, max_length=50, verbose_name='Наименование услуги')
    about = models.TextField(blank=False, max_length=350, verbose_name='О услуге')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-id']


class Servicesdop(models.Model):
    title = models.CharField(blank=False, max_length=50, verbose_name='Наименование услуги')
    about = models.TextField(blank=False, max_length=250, verbose_name='О услуге')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доп услуга'
        verbose_name_plural = 'Доп услуги'
        ordering = ['-id']

class Technologies(models.Model):
    title = models.CharField(blank=False, max_length=50, verbose_name='Наименование технологии')
    image = models.ImageField(blank=False, upload_to='techs/', verbose_name='Изображение технологии')
    about = models.TextField(blank=False, max_length=350, verbose_name='О технологии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'
        ordering = ['-id']

class Works(models.Model):
    title = models.CharField(blank=False, max_length=50, verbose_name='Наименование технологии')
    itis = models.CharField(max_length=300, choices = CHOICES, verbose_name='Вид работы')
    image = models.ImageField(blank=False, upload_to='works/', verbose_name='Изображение')
    address = models.CharField(blank=True, max_length=250, verbose_name='Адрес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'
        ordering = ['-id']