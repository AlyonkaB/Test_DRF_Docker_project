from rest_framework import serializers

from shop_product.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id", "title", "price", "image")
