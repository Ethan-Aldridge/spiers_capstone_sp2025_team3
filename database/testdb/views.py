from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from .models import Battery

def home(request):
    return render(
        request,
        'home.html',
        {
            
        }
    )

def inventory(request, name):
    print(request.build_absolute_uri()) #optional
    serial_num = request.GET.get('serial_num')
    if serial_num:
        items = Battery.objects.filter(serial_num=serial_num)
    else:
        items = Battery.objects.all()
    return render(request, 'inventory.html', {'items': items, 'serial_num': serial_num})