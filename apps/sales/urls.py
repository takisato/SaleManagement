from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path('master/', views.master, name="master"),
    path('master/new/', views.master_new, name="master_new"),
    path('master/new/byfile', views.master_new_by_file, name="master_new_by_file"),
    path('master/int:<sale_id>/edit/', views.master_edit, name="master_edit"),
    path('master/int:<sale_id>/delete/', views.master_delete, name="master_delete"),
    path('statistics/', views.statistics, name="statistics"),
]
