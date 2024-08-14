from django.urls import path
from Appyeri import views

urlpatterns = [ 
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('alumnos/', views.alumnos, name='Alumnos'),
    path('practicas/', views.practicas, name='Practicas'),
    path('sugerencias/', views.sugerencias, name='Sugerencias'),
    #path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    #path('alumno-formulario/', views.formulario_alumno, name='AlumnoFormulario'),
    #path('profesor-formulario/', views.formulario_profesor, name='ProfesorFormulario'),
    path('buscar-cursos/', views.buscar_curso, name= 'BuscarCursos'),
]
