from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
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


@require_POST
def item_master_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('items:item_master')
