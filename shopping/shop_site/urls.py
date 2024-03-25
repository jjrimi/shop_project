from django.urls import path
from shop_site  import views
from .views import create_product

urlpatterns = [
        path('', views.index),
        path('read/<id>/', views.read),
        path('create_product/', create_product, name='create_product'),
        path('category/', views.category, name='category'),
        path('get_products/', views.get_products_by_category, name='get_products_by_category'),
]

