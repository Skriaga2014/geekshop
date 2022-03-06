from django.shortcuts import render

# functions = controllers = viewhi


def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - Продукты'
    }
    return render(request, 'products/products.html', context)



