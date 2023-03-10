from django import forms

from products.models import Product, Image, Comment

# class ProductFileUploadClearableInput(forms.ClearableFileInput):
#     template_name = 'form_widgets/clearable_image_input_product.html'


class ProductAdditionForm(forms.ModelForm):
    # images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
    # images = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'main_image', 'tags']
        widgets = {
            'description': forms.Textarea,
        }

class ProductEditForm(ProductAdditionForm):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
