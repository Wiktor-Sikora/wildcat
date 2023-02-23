import django_filters

from products.models import Product

PRODUCT_FILTER_CHOICES = (
    ('Today', 'Today'),
    ('This week', 'This week'),
    ('This month', 'This month'),
    ('All time', 'All time')
)

class ProductFilter(django_filters.FilterSet):
    owner = django_filters.CharFilter(field_name='owner', lookup_expr='icontains', distinct=True)
    tags = django_filters.CharFilter(field_name='tags', lookup_expr='in', distinct=True)
    # date = django_filters.ChoiceFilter(choices=, empty))

    class Meta:
        model = Product
        fields = ['name', 'description']