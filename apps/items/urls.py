from django.urls import path, include
from . import views

app_name = "items"

urlpatterns = [
    path('item_master', views.item_master, name="item_master"),
]
