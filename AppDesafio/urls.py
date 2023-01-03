from django.urls import path
from AppDesafio import views

urlpatterns = [
    path("inicio", views.inicio,name='Inicio'),
    path("busquedaproducto/", views.busquedaPro, name='productos'),
    path("busquedacategoria/", views.busquedaCat, name='categoria'),
    path("busquedavendedor/", views.busquedaVen, name='vendedor'),
    #Productos
    path("productos/list/", views.ProductosList.as_view(), name='Productos'),
    path("productos/create/", views.ProductosCreate.as_view(), name='Agregar Producto'),
    path("productos/edit/<pk>", views.ProductosEdit.as_view(), name='Editar Producto'),
    path("productos/detail/<pk>", views.ProductosDetail.as_view(), name='Ver Producto'),
    path("productos/delete/<pk>", views.ProductosDelete.as_view(), name='Eliminar Producto'),
    #Categorias
    path("categorias/list/", views.CategoriasList.as_view(), name='Categorias'),
    path("categorias/create/", views.CategoriasCreate.as_view() ,name='Agregar Categoria'),
    path("categorias/edit/<pk>", views.CategoriasEdit.as_view(), name='Editar Categoria'),
    path("categorias/detail/<pk>", views.CategoriasDetail.as_view(), name='Ver Categoria'),
    path("categorias/delete/<pk>", views.CategoriasDelete.as_view(), name='Eliminar Categoria'),
    #Vendedores
    path("vendedores/list/", views.VendedoresList.as_view(), name='Vendedores'),
    path("vendedores/create/", views.VendedoresCreate.as_view() ,name='Agregar Vendedor'),
    path("vendedores/edit/<pk>", views.VendedoresEdit.as_view(), name='Editar Vendedor'),
    path("vendedores/detail/<pk>", views.VendedoresDetail.as_view(), name='Ver Vendedor'),
    path("vendedores/delete/<pk>", views.VendedoresDelete.as_view(), name='Eliminar Vendedor'),




]
