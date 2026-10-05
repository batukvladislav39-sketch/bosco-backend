from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.show_products, name='products'),
    path('products/add/', views.add_product, name='add_product'),
    path('replenish/<int:count>/', views.replenish, name='replenish'),
]