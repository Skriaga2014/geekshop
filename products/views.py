from django.shortcuts import render

# functions = controllers = viewhi


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'Geekshop - Текстовый контекст',
        'header': 'Welcome!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 6090},
        ],
        'is_promotion': True,

    }

    return render(request, 'products/test-context.html', context)

