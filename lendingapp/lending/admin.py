from django.contrib import admin
from .models import Services, Servicesdop, Technologies, Works, Calculate
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):# настройка отображения в админке
    list_display = ('title',)


admin.site.register(Services, ServicesAdmin)

class ServicesdopAdmin(admin.ModelAdmin):# настройка отображения в админке
    list_display = ('title', )

admin.site.register(Servicesdop, ServicesdopAdmin)

class TechnologiesAdmin(admin.ModelAdmin):# настройка отображения в админке
    list_display = ('title', 'image')
    fields = ('title', )

admin.site.register(Technologies, ServicesdopAdmin)

class WorksAdmin(admin.ModelAdmin):# настройка отображения в админке
    list_display = ('title', 'itis', 'image', 'address')

admin.site.register(Works, ServicesdopAdmin)

class CalculateAdmin(admin.ModelAdmin):# настройка отображения в админке
    list_display = ('title', 'cost',)
    fields = ('title', 'cost',)

admin.site.register(Calculate, ServicesAdmin)