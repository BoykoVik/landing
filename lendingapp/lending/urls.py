from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'lending'

urlpatterns = [
    path('', views.index, name='index'),
]