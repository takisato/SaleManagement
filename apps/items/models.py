from django.db import models


class Item(models.Model):
    '''商品'''
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
