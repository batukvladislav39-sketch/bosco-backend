from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.show_products),
    path('replenish/<int:count>/', views.replenish),
]