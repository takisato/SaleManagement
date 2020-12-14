from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Item
from .forms import SaleForm
from django.views.decorators.http import require_POST
from django.contrib import messages
import csv
from io import TextIOWrapper


def master(request):
    sales = Sale.get_all_objets('-created_at')
    return render(request, 'sales/master.html', {'sales': sales})


def master_new(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.profit = sale.item.price*sale.num
            sale.save()

        return redirect('sales:master')
    else:
        form = SaleForm()
    return render(request, 'sales/master_new.html', {'form': form})


def master_new_by_file(request):
    try:
        file_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(file_data)
    except:
        messages.success(request, "error")
        return redirect('sales:master')

    for line in csv_file:
        form = SaleForm()
        sale = form.save(commit=False)
        sale.item = Item.get_objects(line[0])
        sale.num = line[1]
        sale.profit = line[2]
        sale.created_at = line[3]
        sale.save()
    return redirect('sales:master')


def master_edit(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        breakpoint()
        if form.is_valid():
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
