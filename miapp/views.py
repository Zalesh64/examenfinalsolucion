from django.shortcuts import render, redirect
from miapp.forms import formdocente
from miapp.models import Docente


# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')

def integrantes(request):

    return render(request, 'integrantes.html')

def crearCurso(request):

    return render(request, 'crearCurso.html')

def listarCurso(request):

    return render(request, 'listarCurso.html')

def crearDocente(request):
    formulario = formdocente()
    return render(request, 'crearDocente.html', {'form':formulario})

def guardardocente(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    Apellido_Paterno=request.POST['Apellido_Paterno']
    Apellido_Materno=request.POST['Apellido_Materno']
    DNI=request.POST['DNI']
    Fecha_Nacimiento=request.POST['Fecha_Nacimiento']
    Estado=request.POST['Estado']

    docente = Docente(
        codigo=codigo,
        nombre=nombre,
        Apellido_Paterno=Apellido_Paterno,
        Apellido_Materno=Apellido_Materno,
        DNI=DNI,
        Fecha_Nacimiento=Fecha_Nacimiento,
        Estado=Estado
    )
    docente.save()
    return redirect('listarDocente')
    
def listarDocente(request):
    docentes=Docente.objects.all()

    return render(request, 'listarDocente.html', {'docentes':docentes})

def EliminarDocente(request, id):

    docente = Docente.objects.get(pk=id)
    docente.delete()
    return redirect('listarDocente')