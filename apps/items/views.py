from django.shortcuts import render
from .models import Item

def item_master(request):
    items=Item.objects.all().order_by('-id')
    return render(request,'items/item_master.html',{'items':items})
