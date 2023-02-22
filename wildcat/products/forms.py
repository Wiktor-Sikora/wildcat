from django import forms

from products.models import Product, Image

class ProductAdditionForm(forms.ModelForm):
    # images = MultiImageField(min_num=0, max_num=3)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'main_image']
        widgets = {
            'description': forms.Textarea,
        }
