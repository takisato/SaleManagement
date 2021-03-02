from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Item
from .forms import SaleForm, FileForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
from io import TextIOWrapper
import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


@login_required
def master(request):
    sales = Sale.get_all_objets('-created_at')
    file_form = FileForm()
    return render(request, 'sales/master.html', {'sales': sales, 'file_form': file_form})


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
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        file_data = TextIOWrapper(form.files['files'], encoding='utf-8')
        csv_file = csv.reader(file_data)
    else:
        messages.success(request, "error")
        return redirect('sales:master')

    for line in csv_file:
        Sale.objects.create(
            item=Item.get_objects(line[0]),
            num=line[1],
            profit=line[2],
            created_at=line[3],
        )

    return redirect('sales:master')


def master_edit(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()

        return redirect('sales:master')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'sales/master_edit.html', {'form': form, 'sale': sale})


@require_POST
def master_delete(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale.delete()
    return redirect('sales:master')


@login_required
def statistics(request):
    sales = Sale.get_all_objets()
    profit_all = 0
    for sale in sales:
        profit_all += sale.profit

    # 集計関数
    def totalization(sales, date):
        dic = defaultdict(int)
        dic['date'] = date
        dic['num'] = defaultdict(int)
        dic['profit'] = {}
        # 売り上げ計算
        for sale in sales:
            dic['profit_sum'] += sale.profit
            dic['num'][sale.item] += sale.num
            dic['profit'][sale.item] = sale.profit

        # 内訳の記述
        detail_li = []
        for item in dict(dic['num']).keys():
            p = dic['profit'][item]
            n = dic['num'][item]
            detail_li.append(f'{item}:{p}円({n}個)')
        dic['detail'] = " ".join(detail_li)
        
        return dic

    now = datetime.datetime.now()
    # 月集計
    month_list = []
    distance = 3
    i = 0
    while(i < distance):
        month_sales = Sale.get_objets_by_month(distance=i)
        # 日付の文字列作成
        month_date = now-relativedelta(months=i)
        month_date = month_date.strftime("%Y年%m月")

        month_list.append(totalization(month_sales, month_date))
        i += 1

    # 日集計
    day_list = []
    distance = 3
    i = 0
    while(i < distance):
        day_sales = Sale.get_objets_by_day(i)
        day_date = now-relativedelta(days=i)
        day_date = day_date.strftime("%Y年%m月%d日")
        day_list.append(totalization(day_sales, day_date))
        i += 1

    return render(
        request, 'sales/statistics.html',
        {'profit_all': profit_all,
         'month_list': month_list,
         'day_list': day_list, }
    )
