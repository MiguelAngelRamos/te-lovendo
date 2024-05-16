from django.shortcuts import render
from .models import Producto

def list_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/list_productos.html', { 'productos': productos})
# Create your views here.

def login(request):
    return render(request, 'gestion/login.html', {})
