from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def item_master(request):
    items = Item.objects.all().order_by('-id')
    return render(request, 'items/item_master.html', {'items': items})


def item_master_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            
        return redirect('items:item_master')

    else:
        form = ItemForm()
    return render(request, 'items/item_master_new.html', {'form': form})
