from django.urls import path
from products.views import ProductDetailAPIView, ProductCreateAPIView


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="detail view with primary key"), 
    path('', ProductCreateAPIView.as_view(), name="Create a new instance of product"), 
]


# this was to test str in the slug
# path('<str:title>/', ProductDetailAPIView.as_view(), name="detail view with title"), 