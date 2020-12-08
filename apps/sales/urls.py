from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path('sales_master/',views.master,name="master"),
]
