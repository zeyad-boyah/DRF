from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # on by default but we can change it to title for example to make it work with the other commented view