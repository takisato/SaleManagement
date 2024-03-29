from django.db import models
from apps.items.models import Item
import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Sale(models.Model):
    '''売り上げ'''
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, db_constraint=False)
    profit = models.PositiveIntegerField(null=True,blank=True)
    num = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.item)

    @classmethod
    def get_all_objets(cls, order_field='-profit'):
        return cls.objects.all().order_by(order_field)

    @classmethod
    def get_objets_by_month(cls, date):
        d = date
        year = d.strftime("%Y")
        month = d.strftime("%m")
        return cls.objects.filter(created_at__year=year,created_at__month=month)

    @classmethod
    def get_objets_by_day(cls, date):
        d = date
        year = d.strftime("%Y")
        month = d.strftime("%m")
        date = d.strftime("%d")
        return cls.objects.filter(created_at__year=year,created_at__month=month,created_at__day=date)
