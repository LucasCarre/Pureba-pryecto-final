from django.shortcuts import render
from django.http import HttpResponse
from Appyeri.models import *
from Appyeri.forms import *

def inicio(request):
    return render(request, 'appyeri/inicio.html')

def profesores(request):
    if request.method == 'POST':
        prof_formulario = Profesor_formulario(request.POST)
        print(prof_formulario)
        
        if prof_formulario.is_valid():
            informacion= prof_formulario.cleaned_data
            profesor= Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            profesor.save()
            return render(request, 'appyeri/inicio.html')
    else:
        prof_formulario = Profesor_formulario()
    return render(request, 'appyeri/profesores.html', {'prof_formulario':prof_formulario})

def practicas(request):
    return render(request, 'appyeri/practicas.html')

def sugerencias(request):
    if request.method == 'POST':

        sugerencia = Sugerencias(nombre_del_curso=request.POST['nombre del curso'],modalidad=request.POST['modalidad'])
        sugerencia.save()

        return render(request, "appyeri/inicio.html")
    return render(request, 'appyeri/sugerencias.html',)

def cursos(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "appyeri/inicio.html")

    return render(request,"appyeri/cursos.html")

def alumnos(request):
    if request.method == 'POST':
        mi_formulario= Alumno_formulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            informacion= mi_formulario.cleaned_data
            alumno= Alumno(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            alumno.save()
            return render(request, 'appyeri/inicio.html')
    else:
        mi_formulario=Alumno_formulario
    return render(request, 'appyeri/alumnos.html',{'mi_formulario':mi_formulario})

def buscar_curso(request):
    if request.method == "POST":
        mi_formulario = Buscar_cursos(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appyeri/mostrar-cursos.html", {"cursos": cursos})
    else:
        mi_formulario = Buscar_cursos()

    return render(request, "appyeri/buscar-cursos.html", {"mi_formulario": mi_formulario})
