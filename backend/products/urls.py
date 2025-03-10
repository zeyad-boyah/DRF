from django.urls import path
from products.views import ProductDetailAPIView


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="detail view with primary key"), 
]


# this was to test str in the slug
# path('<str:title>/', ProductDetailAPIView.as_view(), name="detail view with title"), 