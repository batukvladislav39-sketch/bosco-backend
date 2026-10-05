from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.show_products),
    path('products/add/', views.add_product),
    path('replenish/<int:count>/', views.replenish),
]