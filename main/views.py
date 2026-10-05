from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import random

# Create your views here.

def home(request):
    return HttpResponse("""
        <h1>Welcome to Warehouse</h1>
        <p>Warehouse Management System</p>
        <a href="/products/">View Products</a>
    """)

def show_products(request):
    products = Product.objects.all()

    return render(
        request,
        "main/products.html",
        {"products": products}
    )

def replenish(request, count):
    names = ["T-Shirt", "Jeans", "Jacket", "Hoodie", "Shirt"]
    brands = ["Nike", "Adidas", "Puma", "Zara", "H&M"]
    sizes = ["S", "M", "L", "XL"]
    colors = ["Black", "White", "Red", "Blue", "Green"]

    for i in range(count):
        Product.objects.create(
            name=random.choice(names),
            brand=random.choice(brands),
            size=random.choice(sizes),
            color=random.choice(colors),
            price=random.randint(500, 5000)
        )

    return HttpResponse(f"Додано {count} нових записів")
