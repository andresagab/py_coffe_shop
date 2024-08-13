from django import forms
from django.forms import ModelForm

from ..models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=[(item['key'], item['name']) for item in Order.STATUS_TYPES]),
        }
