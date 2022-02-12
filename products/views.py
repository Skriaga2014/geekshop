from django.shortcuts import render

# functions = controllers = viewhi

def index(request):
    return render(request, 'products/index.html')

