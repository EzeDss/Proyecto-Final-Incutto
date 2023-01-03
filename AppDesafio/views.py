from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from AppDesafio.models import Productos
from AppDesafio.models import Categorias
from AppDesafio.models import Vendedores

# Create your views here.
def inicio(request):
    return render(request,'AppDesafio/inicio.html')    

#Productos
def busquedaPro(request):
    busqueda = request.GET.get('producto')
    print(busqueda)
    res_a = Productos.objects.filter(producto = busqueda)
    return render(request,'AppDesafio/resultadopro.html',{"busqueda": busqueda, "productos": res_a})

class ProductosList(ListView):
    model = Productos
    template = 'AppDesafio/productos_list.html'

class ProductosCreate(CreateView):
    model = Productos
    fields = '__all__'
    success_url = '/AppDesafio/productos/list/'

class ProductosEdit(UpdateView):
    model = Productos
    fields = '__all__'
    success_url = '/AppDesafio/productos/list/'

class ProductosDetail (DetailView):
    model = Productos
    template_name = 'AppDesafio/productos_detail.html'

class ProductosDelete(DeleteView):
    model = Productos
    success_url = '/AppDesafio/productos/list/'

#Categorias
def busquedaCat(request):
    busqueda = request.GET.get('categoria')
    print(busqueda)
    res_a = Categorias.objects.filter(categoria = busqueda)
    return render(request,'AppDesafio/resultadocat.html',{"busqueda": busqueda, "categoria": res_a})

class CategoriasList(ListView):
    model = Categorias
    template = 'AppDesafio/categorias_list.html'

class CategoriasCreate(CreateView):
    model = Categorias
    fields = '__all__'
    success_url = '/AppDesafio/categorias/list/'

class CategoriasEdit(UpdateView):
    model = Categorias
    fields = '__all__'
    success_url = '/AppDesafio/categorias/list/'

class CategoriasDetail (DetailView):
    model = Categorias
    template_name = 'AppDesafio/categorias_detail.html'

class CategoriasDelete(DeleteView):
    model = Categorias
    success_url = '/AppDesafio/categorias/list/'

#Vendedores
def busquedaVen(request):
    busqueda = request.GET.get('vendedor')
    print(busqueda)
    res_a = Vendedores.objects.filter(nombre = busqueda)
    return render(request,'AppDesafio/resultadoven.html',{"busqueda": busqueda, "vendedor": res_a})

class VendedoresList(ListView):
    model = Vendedores
    template = 'AppDesafio/vendedores_list.html'

class VendedoresCreate(CreateView):
    model = Vendedores
    fields = '__all__'
    success_url = '/AppDesafio/vendedores/list/'

class VendedoresEdit(UpdateView):
    model = Vendedores
    fields = '__all__'
    success_url = '/AppDesafio/vendedores/list/'

class VendedoresDetail (DetailView):
    model = Vendedores
    template_name = 'AppDesafio/vendedores_detail.html'

class VendedoresDelete(DeleteView):
    model = Vendedores
    success_url = '/AppDesafio/vendedores/list/'