from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from aves_argentinas.models import Aves, Fauna, Flora
from aves_argentinas.forms import AveFormulario, FaunaFormulario, FloraFormulario
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
# Create your views here.

#Crear nueva publicacion de cada clase:

def crear_aves(request):
    if request.method == 'POST':
        formulario = AveFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            orden = data['orden']
            familia = data['familia']
            especie = data['especie']
            caracteristicas = data['caracteristicas']
            ultima_observacion = data['ultima_observacion']
            ave = Aves(nombre=nombre, orden=orden, familia=familia, especie=especie, caracteristicas=caracteristicas, ultima_observacion=ultima_observacion)
            ave.save()
            
            url_exitosa = reverse('lista_aves')
            return redirect(url_exitosa)
    else:
        formulario = AveFormulario()
    http_response = render(
        request = request,
        template_name='aves_argentinas/formulario_aves.html',
        context={'formulario' : formulario}
    )
    return http_response

def crear_fauna(request):
    if request.method == 'POST':
        formulario = FaunaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            orden = data['orden']
            familia = data['familia']
            especie = data['especie']
            caracteristicas = data['caracteristicas']
            ultima_observacion = data['ultima_observacion']
            fauna = Fauna(nombre=nombre, orden=orden, familia=familia, especie=especie, caracteristicas=caracteristicas, ultima_observacion=ultima_observacion)
            fauna.save()
            
            url_exitosa = reverse('lista_fauna')
            return redirect(url_exitosa)
    else:
        formulario = FaunaFormulario()
    http_response = render(
        request = request,
        template_name='aves_argentinas/formulario_fauna.html',
        context={'formulario' : formulario}
    )
    return http_response

def crear_flora(request):
    if request.method == 'POST':
        formulario = FloraFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            especie = data['especie']
            caracteristicas = data['caracteristicas']
            tipo = data['tipo']
            flora = Flora(nombre=nombre, especie=especie, caracteristicas=caracteristicas, tipo=tipo)
            flora.save()
            
            url_exitosa = reverse('lista_flora')
            return redirect(url_exitosa)
    else:
        formulario = FloraFormulario()
    http_response = render(
        request = request,
        template_name='aves_argentinas/formulario_flora.html',
        context={'formulario' : formulario}
    )
    return http_response


#Mostrar clases en la pagina:
def mostrar_aves(request):
    contexto = {
        "aves" : Aves.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='aves_argentinas/mostrar_aves.html',
        context=contexto,
    )
    return http_response

def mostrar_fauna(request):
    contexto = {
        "faunas" : Fauna.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='aves_argentinas/mostrar_fauna.html',
        context=contexto,
    )
    return http_response

def mostrar_flora(request):
    contexto = {
        "floras" : Flora.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='aves_argentinas/mostrar_flora.html',
        context=contexto,
    )
    return http_response


#Buscar por dato

def buscar_aves(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        aves = Aves.objects.filter(nombre__contains=busqueda)
        contexto = {
            "aves" : aves,
        }
        http_response = render(
            request = request,
            template_name='aves_argentinas/mostrar_aves.html',
            context = contexto,
        )
        return http_response
    
def buscar_fauna(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        fauna = Fauna.objects.filter(nombre__contains=busqueda)
        contexto = {
            "faunas" : fauna,
        }
        http_response = render(
            request = request,
            template_name='aves_argentinas/mostrar_fauna.html',
            context = contexto,
        )
        return http_response
    
def buscar_flora(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        flora = Flora.objects.filter(nombre__contains=busqueda)
        contexto = {
            "floras" : flora,
        }
        http_response = render(
            request = request,
            template_name='aves_argentinas/mostrar_flora.html',
            context = contexto,
        )
        return http_response
    
def eliminar_aves(request, id):
    ave = Aves.objects.get(id=id)
    if request.method == 'POST':
        ave.delete()
        url_exitosa = reverse('lista_aves')
        return redirect(url_exitosa)
    
def eliminar_fauna(request, id):
    fauna = Fauna.objects.get(id=id)
    if request.method == 'POST':
        fauna.delete()
        url_exitosa = reverse('lista_fauna')
        return redirect(url_exitosa)
    
def eliminar_flora(request, id):
    flora = Flora.objects.get(id=id)
    if request.method == 'POST':
        flora.delete()
        url_exitosa = reverse('lista_flora')
        return redirect(url_exitosa)
    
def editar_aves(request, id):
    ave = Aves.objects.get(id=id)
    if request.method == 'POST':
        formulario = AveFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            ave.nombre = data['nombre']
            ave.orden = data['orden']
            ave.familia = data['familia']
            ave.especie = data['especie']
            ave.caracteristicas = data['caracteristicas']
            ave.ultima_observacion = data['ultima_observacion']
            ave.save()
            url_exitosa = reverse('lista_aves')
            return redirect(url_exitosa)
    else:
        inicial = { #le paso al form esta data inicial para que aparezcan los datos completados al ingresar a 'editar' y luego los puedo modificar
            'nombre' : ave.nombre,
            'orden' : ave.orden,
            'familia' : ave.familia,
            'especie' : ave.especie, 
            'caracteristicas' : ave.caracteristicas,
            'ultima_observacion' : ave.ultima_observacion,
        }
        formulario = AveFormulario(initial=inicial)
        return render(
            request=request,
            template_name='aves_argentinas/formulario_aves.html',
            context={'formulario': formulario},
        )
        
def editar_fauna(request, id):
    fauna = Fauna.objects.get(id=id)
    if request.method == 'POST':
        formulario = FaunaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            fauna.nombre = data['nombre']
            fauna.orden = data['orden']
            fauna.familia = data['familia']
            fauna.especie = data['especie']
            fauna.caracteristicas = data['caracteristicas']
            fauna.ultima_observacion = data['ultima_observacion']
            fauna.save()
            url_exitosa = reverse('lista_fauna')
            return redirect(url_exitosa)
    else:
        inicial = { #le paso al form esta data inicial para que aparezcan los datos completados al ingresar a 'editar' y luego los puedo modificar
            'nombre' : fauna.nombre,
            'orden' : fauna.orden,
            'familia' : fauna.familia,
            'especie' : fauna.especie, 
            'caracteristicas' : fauna.caracteristicas,
            'ultima_observacion' : fauna.ultima_observacion,
        }
        formulario = FaunaFormulario(initial=inicial)
        return render(
            request=request,
            template_name='aves_argentinas/formulario_fauna.html',
            context={'formulario': formulario},
        )
        
def editar_flora(request, id):
    flora = Flora.objects.get(id=id)
    if request.method == 'POST':
        formulario = FloraFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            flora.nombre = data['nombre']
            flora.especie = data['especie']
            flora.caracteristicas = data['caracteristicas']
            flora.tipo = data['tipo']
            flora.save()
            url_exitosa = reverse('lista_flora')
            return redirect(url_exitosa)
    else:
        inicial = { #le paso al form esta data inicial para que aparezcan los datos completados al ingresar a 'editar' y luego los puedo modificar
            'nombre' : flora.nombre,
            'especie' : flora.especie, 
            'caracteristicas' : flora.caracteristicas,
            'tipo' : flora.tipo,
        }
        formulario = FloraFormulario(initial=inicial)
        return render(
            request=request,
            template_name='aves_argentinas/formulario_flora.html',
            context={'formulario': formulario},
        )
   
class AvesDetailView(DetailView):
   model = Aves
   success_url = reverse_lazy('lista_aves')
   
class FaunaDetailView(DetailView):
   model = Fauna
   success_url = reverse_lazy('lista_fauna')
   
class FloraDetailView(DetailView):
   model = Flora
   success_url = reverse_lazy('lista_flora')

