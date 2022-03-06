from django.shortcuts import render

# functions = controllers = viewhi



def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'products/index.html', context)


def products(request):

    context = {
        'title': 'Geekshop - Продукты',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090, 'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'link': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': 23725, 'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'link': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390, 'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340, 'desc': 'Плотная ткань. Легкий материал.', 'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590, 'desc': 'Гладкий кожаный верх. Натуральный материал.', 'link': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890, 'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ]
    }
    return render(request, 'products/products.html', context)


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

