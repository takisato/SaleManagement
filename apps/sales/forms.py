from django.forms import Form, FileField, ModelForm, SelectDateWidget
from .models import Sale
from django.core.validators import FileExtensionValidator


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['item', 'num', 'created_at', 'profit']
        widgets = {
            'created_at': SelectDateWidget
        }


class FileForm(Form):
    files = FileField(required=True,validators=[FileExtensionValidator(['csv'])])

