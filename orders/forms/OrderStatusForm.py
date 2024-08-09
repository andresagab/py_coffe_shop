from django.forms import ModelForm, forms

from orders.models import Order


class OrderStatusForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'status',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OrderStatusForm, self).__init__(*args, **kwargs)

    def clean_status(self):
        status = self.cleaned_data.get('status')
        available_statuses = ['CO', 'CA']

        if status not in available_statuses:
            raise forms.ValidationError('Invalid status')
        else:
            order = Order.objects.filter(is_active=True, user=self.request.user).first()

            if not order:
                raise forms.ValidationError('You do not have an active order')
            if order and order.status == status:
                raise forms.ValidationError('The status is already set')
            elif order and order.status not in available_statuses and order.status != 'UC':
                raise forms.ValidationError('The order cannot longer be modified')
            elif order and order.status == 'CA' and status == 'CO':
                raise forms.ValidationError('The order is already canceled')
            elif order and order.status == 'CO' and status == 'CA':
                raise forms.ValidationError('The order is already confirmed')

        return status
