from rest_framework import pagination

class ProductPagination(pagination.PageNumberPagination):
    page_size = 20