from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from django_filters import rest_framework as filters

from api.serializers import ProductSerializer
from api.pagination import ProductPagination
from api.filters import ProductFilter

from products.models import Product
from time import sleep

User = get_user_model()


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class AddStarApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def put(self, request, pk=None, *args, **kwargs):
        '''adds star to item'''
        product_instance = self.get_object(pk)
        
        if not product_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if product_instance.stars.filter(pk=request.user.id).exists():
            return Response({'res': 'You have already starred this product'}, status=status.HTTP_400_BAD_REQUEST)

        product_instance.stars.add(request.user)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk=None, *args, **kwargs):
        '''delete star from item'''
        product_instance = self.get_object(pk)

        if not product_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if not product_instance.stars.filter(pk=request.user.pk).exists():
            return Response({'res': 'you do not have a star on this product'}, status=status.HTTP_400_BAD_REQUEST)

        product_instance.stars.remove(request.user)
        return Response(status=status.HTTP_200_OK)


class FollowUserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def put(self, request, pk=None, *args, **kwargs):
        '''adds star to item'''
        user_instance = self.get_object(pk)
        
        if not user_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if user_instance.follows.filter(pk=request.user.id).exists():
            return Response({'res': 'You have already followed this account'}, status=status.HTTP_400_BAD_REQUEST)

        user_instance.follows.add(request.user, )
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk=None, *args, **kwargs):
        '''delete star from item'''
        user_instance = self.get_object(pk)

        if not user_instance:
            return Response({'res': 'object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if not user_instance.follows.filter(pk=request.user.pk).exists():
            return Response({'res': 'you do not have a follow on this user'}, status=status.HTTP_400_BAD_REQUEST)

        user_instance.follows.remove(request.user)
        return Response(status=status.HTTP_200_OK)

