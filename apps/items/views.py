from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Item
from .forms import ItemForm


def item_master(request):
    items = Item.get_all_objets('-updated_at')
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


def item_master_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:item_master')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_master_edit.html', {'form': form, 'item': item})


@require_POST
def item_master_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('items:item_master')
