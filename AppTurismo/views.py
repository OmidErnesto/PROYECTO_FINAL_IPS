from AppTurismo.forms import ZonaTuristicaForm, RegistroForm
from django.shortcuts import redirect, render
from AppTurismo.models import ZonaTuristica, UsuarioCliente
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

def myHomeView(request):
    return render(request,'base.html',{})

def CrearZonaTuristica(request):
    form = ZonaTuristicaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = ZonaTuristicaForm()
        else:
            print("No creado")
    context = {
        'form' : form
    }
    return render(request,'AppTurismo/ZonaCreate.html',context)


def BorrarZonaTuristica(request, myTitle):
    obj = ZonaTuristica.objects.get(nombre = myTitle)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'objeto':obj,
    }
    return render(request, 'AppTurismo/borrarZonaTuristica.html', context)

class ZonaTuristicaListView(ListView):
    model = ZonaTuristica

class ZonaTuristicaRegistro(CreateView):
    model = ZonaTuristica
    form_class = ZonaTuristicaForm
    template_name = 'AppTurismo/ZonaCreate.html'
    success_url = '/zonaturismo/'


class ZonaTuristicaDetailsView(DetailView):
    model = ZonaTuristica


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('../')
        else:
            messages.info(request,'Datos invalidos')
            return redirect('../login')

    else:
         return render(request,'Usuario/login.html')

def logout(request):
    auth.logout(request)
    return redirect('../')

def ZonaTuristicaEdit(request,myTitle):
    zonaTur = ZonaTuristica.objects.get(nombre = myTitle)
    if request.method == 'GET':
        form = ZonaTuristicaForm(instance=zonaTur)
    else:
        form = ZonaTuristicaForm(request.POST, instance=zonaTur)
        if form.is_valid():
            form.save()
            #ZonaTuristica.objects.get(nombre = myTitle).delete()
        return redirect('/zonaturismo/')

    context = {
        'form':form,
    }

    return render(request,'AppTurismo/ZonaCreate.html',context)

class RegistroUsuario(CreateView):
    model = UsuarioCliente
    template_name = 'Usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('AppTurismo:zonaturismo-list')

def myHomeView2(request):
    return render(request,'usuario_view.html',{})