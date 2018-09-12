from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User
from .models import Asesoria


def index(request):
    tipo = 0
    agregar = 0
    return render(request, 'register/index.html')

def registro(request):
    return render(request, 'register/registro.html')

def register(request):
    a=request.POST['last_name']
    print(a)
    errors = User.objects.validator(request.POST)
    #print(len(errors))
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/registro')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            agregar = 0
            tipo = 0
            return redirect('/listarAsesoria')
    return redirect('/')

def agregarAsesoria(request):
    agregar = 1
    tipo = 0
    listado = Asesoria.objects.all()
    return render(request, 'register/listarAsesoria.html', locals())

def add(request):
    tipo = 0
    agregar = 0
    asesoria = Asesoria.objects.create(curso=request.POST['curso'], profesor=request.POST['profesor'], horario=request.POST['horario'], lugar=request.POST['lugar'])
    asesoria.save()
    return redirect('/listarAsesoria')

def listarAsesoria(request):
    tipo = 0
    agregar = 0
    listado = Asesoria.objects.all().order_by("id")
    return render(request, 'register/listarAsesoria.html', locals())

def eliminarAsesoria(request):
    tipo = 0
    agregar = 0
    id=request.POST.get('id_asesoria', False)
    Asesoria.objects.filter(id=id).delete()
    return redirect('/listarAsesoria')

def editarAsesoria(request):
    id = int(request.GET.get('id'))
    tipo= 1
    agregar= 0
    listado = Asesoria.objects.all().order_by("id")
    return render(request, 'register/listarAsesoria.html', locals())

def guardarCambios(request):
    tipo = 0
    agregar = 0
    id=request.POST.get('id_asesoria', False)
    curso=request.POST['curso']
    profesor=request.POST['profesor']
    horario=request.POST['horario']
    lugar=request.POST['lugar']
    asesoria= Asesoria.objects.get(id=id)
    asesoria.curso = curso
    asesoria.profesor = profesor
    asesoria.horario = horario
    asesoria.lugar = lugar
    asesoria.save()
    return redirect('/listarAsesoria')

def cancelar(request):
    tipo = 0
    agregar = 0
    return redirect('/listarAsesoria')

def salir(request):
    tipo = 0
    agregar = 0
    return redirect('/')
