from django.shortcuts import render
from django.http import HttpResponse
from Appyeri.models import *
from Appyeri.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class AlumnoListView(ListView):
    model = Alumno
    context_object_name= "Alumnos"
    template_name= "Appyeri/lista_alumnos.html"

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = "Appyeri/alumno_borrar.html"
    success_url = reverse_lazy("ListarAlumnos") 


class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = "Appyeri/actualizar_alumnos.html"
    success_url = reverse_lazy("ListarAlumnos")
    fields= ["nombre", "apellido"]

class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = "Appyeri/agregar_alumno.html"
    success_url = reverse_lazy("ListarAlumnos")
    fields= ["nombre", "apellido"]

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    context_object_name= "Cursos"
    template_name= "Appyeri/lista_cursos.html"

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "Appyeri/curso_borrar.html"
    success_url = reverse_lazy("ListarCursos") 


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "Appyeri/actualizar_curso.html"
    success_url = reverse_lazy("ListarCursos")
    fields= ["nombre", "camada"]

class CursoCreateView(CreateView):
    model = Curso
    template_name = "Appyeri/agregar_curso.html"
    success_url = reverse_lazy("ListarCursos")
    fields= ["nombre", "camada"]

class ProfesorListView(ListView):
    model = Profesor
    context_object_name= "Profesores"
    template_name= "Appyeri/lista_profesores.html"

class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = "Appyeri/agregar_profesor.html"
    success_url = reverse_lazy("ListarProfesores")
    fields= ["nombre", "apellido", "email"]

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = "Appyeri/borrar_profesror.html"
    success_url = reverse_lazy("ListarProfesores") 