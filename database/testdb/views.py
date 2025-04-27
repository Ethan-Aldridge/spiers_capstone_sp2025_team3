from django.shortcuts import render
from .models import Battery
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', { })

@login_required
def inventory(request):
    print(request.build_absolute_uri()) #optional

    # Get the user's group names
    user_groups = request.user.groups.values_list('name', flat=True)
    locations = ['Warehouse A', 'Warehouse B', 'Warehouse C']
    accessible_locations = [local for local in locations if local in user_groups]

    # Get query parameters
    serial_num = request.GET.get('serial_num')
    location = request.GET.get('location')

    # Filter items based on location and serial number
    items = Battery.objects.filter(location__in=accessible_locations)

    if location:
        items = items.filter(location=location)

    if serial_num:
        items = items.filter(serial_num=serial_num)

    items = items.filter(location__in=accessible_locations)

    return render(request, 'inventory.html', {
        'items': items,
        'accessible_locations': accessible_locations,
        'serial_num': serial_num,
        'location': location})