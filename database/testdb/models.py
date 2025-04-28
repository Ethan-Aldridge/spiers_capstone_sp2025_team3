from django.db import models
from django.utils.timezone import now

class Battery(models.Model):
    serial_num = models.IntegerField(primary_key=True)
    part_num = models.IntegerField()
    item_type = models.CharField(max_length=60)
    user_ID = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    madlibs = models.TextField()
    image = models.ImageField(upload_to='inventory/images/') # TODO: fix saving and display of images

class WarehouseA(models.Model):
    serial_num = models.IntegerField(primary_key=True)
    part_num = models.IntegerField()
    item_type = models.CharField(max_length=60)
    user_ID = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    madlibs = models.TextField()
    image = models.ImageField(upload_to='images/') # TODO: fix saving and display of images

class WarehouseB(models.Model):
    serial_num = models.IntegerField(primary_key=True)
    part_num = models.IntegerField()
    item_type = models.CharField(max_length=60)
    user_ID = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    madlibs = models.TextField()
    image = models.ImageField(upload_to='images/') # TODO: fix saving and display of images

class WarehouseC(models.Model):
    serial_num = models.IntegerField(primary_key=True)
    part_num = models.IntegerField()
    item_type = models.CharField(max_length=60)
    user_ID = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    madlibs = models.TextField()
    image = models.ImageField(upload_to='images/') # TODO: fix saving and display of images