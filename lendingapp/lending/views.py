from django.shortcuts import render
from .models import Services, Servicesdop, Technologies, Works

# Create your views here.

def index(request):
    servs = Services.objects.order_by('id')
    servsdop = Servicesdop.objects.all().order_by('id')
    techs = Technologies.objects.all().order_by('id')
    return render(request, 'lending/index.html', {'servs': servs, 'servsdop': servsdop, 'techs': techs})
