from django import forms

from products.models import Product, Image, Comment

class ProductFileUploadClearableInput(forms.ClearableFileInput):
    template_name = 'form_widgets/clearable_image_input_product.html'


class ProductAdditionForm(forms.ModelForm):
    # images = MultiImageField(min_num=0, max_num=3)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    main_image = forms.ImageField(widget=forms.ClearableFileInput(), required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'main_image']
        widgets = {
            'description': forms.Textarea,
        }

class ProductEditForm(ProductAdditionForm):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


# class 