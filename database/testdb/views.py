from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from .models import Battery

def home(request):
    return render(request, 'home.html', { })

def inventory(request):
    print(request.build_absolute_uri()) #optional
    serial_num = request.GET.get('serial_num')
    location = request.GET.get('location')
    if serial_num and location:
        items = Battery.objects.filter(serial_num=serial_num, location=location)
    elif serial_num:
        items = Battery.objects.filter(serial_num=serial_num)
    elif location:
        items = Battery.objects.filter(location=location)
    else:
        items = Battery.objects.all()
    return render(request, 'inventory.html', {'items': items, 'serial_num': serial_num, 'location': location})