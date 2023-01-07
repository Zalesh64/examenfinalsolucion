from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')

def integrantes(request):

    return render(request, 'integrantes.html')

def crearCurso(request):

    return render(request, 'crearCurso.html')

def listarCurso(request):

    return render(request, 'listarCurso.html')

def listarDocente(request):

    return render(request, 'listarDocente.html')

def crearDocente(request):

    return render(request, 'crearDocente.html')

