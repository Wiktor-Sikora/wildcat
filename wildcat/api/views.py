from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

from api.serializers import ProductSerializer
from api.pagination import ProductPagination
from api.filters import ProductFilter

from products.models import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_class = ProductFilter


class AddStarApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def put(self, request, product_id, *args, **kwargs):
        '''adds star to item'''
        product_instance = self.get_object(product_id)
        
        if not product_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if product_instance.stars_set.filter(user=request.user.id).exists():
            return Response({'res': 'You have already starred this product'}, status=status.HTTP_400_BAD_REQUEST)

        product_instance.stars.add(request.user)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, product_id, *args, **kwargs):
        '''delete star from item'''
        product_instance = self.get_object(product_id)
        
        if not product_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if not product_instance.stars_set.filter(user=request.user.id).exists():
            return Response({'res': 'you do not have a star on this product'}, status=status.HTTP_400_BAD_REQUEST)

        product_instance.stars.remove(request.user)
        return Response(status=status.HTTP_200_OK)
