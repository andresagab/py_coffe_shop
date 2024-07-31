from django.forms import ModelForm, forms

from products.models import ProductRating


class ProductRatingForm(ModelForm):
    class Meta:
        model = ProductRating
        # form fields
        fields = [
            'product',
            'rating',
            'comment'
        ]

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5')
        return rating

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) > 500:
            raise forms.ValidationError('Comment must be less than 500 characters')
        elif not comment:
            raise forms.ValidationError('Comment is required')
        return comment