from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from .forms import SaleForm
from django.views.decorators.http import require_POST


def master(request):
    sales = Sale.get_all_objets('-created_at')
    return render(request, 'sales/master.html', {'sales': sales})


def master_new(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.price = sale.item.price
            sale.profit = sale.price*sale.num
            sale.save()

        return redirect('sales:master')
    else:
        form = SaleForm()
    return render(request, 'sales/master_new.html', {'form': form})


def master_edit(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.profit = sale.price*sale.num
            sale.save()

        return redirect('sales:master')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sales/master_edit.html', {'form': form, 'sale': sale})


@require_POST
def master_delete(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale.delete()
    return redirect('sales:master')
