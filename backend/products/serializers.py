from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    the_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "sale_price",
            "the_number",
        ]

    def get_the_number(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.funny_number()


"""
this does the exactly the same and funny_number even thought it is an instance method works because 
DRF detects that the attribute is callable and, if so, calls it automatically to get its return value.
"""
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'description',
#             'price',
#             'sale_price',
#             'funny_number',
#         ]
