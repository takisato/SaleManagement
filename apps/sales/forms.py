from django.forms import ModelForm, SelectDateWidget
from .models import Sale


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['item', 'num', 'created_at', 'profit', ]
        widgets = {
            'created_at': SelectDateWidget
        }
