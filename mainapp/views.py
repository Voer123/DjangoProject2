from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):
    content = {
        'title': 'GeekShop - Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Товар',
        'products': Product.objects.all(),
        'ProductCategory': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', content)