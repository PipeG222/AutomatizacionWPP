from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from .forms import FormularioRegistro #Formulario creado para creacion de usuario


def home(request):
    return render(request,"home.html")

@login_required
def products(request):
    return render (request,"products.html")

def login_view(request):
    
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
            
        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        else:
            messages.error(request,('Error al iniciar sesión'))
            return redirect(reverse('login'))
        
    if request.method == "GET":
        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def register_view(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Error al registrarse, por favor intente de nuevo.')
            return redirect(reverse('register'))

    elif request.method == 'GET':
        formulario = FormularioRegistro()

    return render(request, 'register.html', {'formulario': formulario})

        