from django.db import models
from apps.items.models import Item
import datetime


class Sale(models.Model):
    '''売り上げ'''
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    profit = models.PositiveIntegerField()
    num = models.PositiveIntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.item)

    @classmethod
    def get_all_objets(cls, order_field='-profit'):
        return cls.objects.all().order_by(order_field)

    @classmethod
    def get_objets_by_month(cls, distance=1):
        now = datetime.datetime.now()
        d = now.month-distance
        return cls.objects.filter(created_at__month=d)

    @classmethod
    def get_objets_by_day(cls, distance=1):
        now = datetime.datetime.now()
        d = now.day-distance
        return cls.objects.filter(created_at__day=d)
