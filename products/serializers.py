from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    name_highlighted = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'name_highlighted']