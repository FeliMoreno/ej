from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'miapp/crear_categoria.html', {'form': form})

def buscar_productos(request):
    query = request.GET.get('q')
    resultados = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'miapp/buscar_productos.html', {'resultados': resultados})

