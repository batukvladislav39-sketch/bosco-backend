from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import random
from django.contrib import messages
from django.shortcuts import render, redirect

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


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        size = request.POST.get("size")
        color = request.POST.get("color")
        price = request.POST.get("price")

        if not all([name, brand, size, color, price]):
            messages.error(request, "All fields are required!")
            return redirect("/products/add/")

        try:
            price = float(price)

            if price <= 0:
                raise ValueError

        except ValueError:
            messages.error(request, "Price must be a positive number!")
            return redirect("/products/add/")

        Product.objects.create(
            name=name,
            brand=brand,
            size=size,
            color=color,
            price=price
        )

        messages.success(request, "Product successfully added!")
        return redirect("/products/")

    return render(request, "main/add_product.html")
