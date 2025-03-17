from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

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
    image = models.ImageField()