from django.shortcuts import render
from rest_framework import viewsets

from shop_product.models import Products
from shop_product.serializers import ProductsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
