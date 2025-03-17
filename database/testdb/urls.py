from django.urls import path
from testdb import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<name>/", views.inventory, name="inventory"),
]
