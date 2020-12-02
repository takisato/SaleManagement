from django.urls import path, include
from . import views

app_name = "items"

urlpatterns = [
    path('item_master/', views.item_master, name="item_master"),
    path('item_master/new/', views.item_master_new, name="item_master_new"),
]
