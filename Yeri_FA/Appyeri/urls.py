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
    path('alumno/listar', views.AlumnoListView.as_view(), name='ListarAlumnos'),
    path('alumno/<pk>/borrar', views.AlumnoDeleteView.as_view(), name='AlumnoBorrar'),
    path('alumno/<pk>/actualizar', views.AlumnoUpdateView.as_view(), name='AlumnoActualizar'),
    path('alumno/agregar', views.AlumnoCreateView.as_view(), name='AgregarAlumno'),
    path('curso/listar', views.CursoListView.as_view(), name='ListarCursos'),
    path('curso/<pk>/detalle', views.CursoDetailView.as_view(), name='DetalleCurso'),
    path('curso/<pk>/borrar', views.CursoDeleteView.as_view(), name='BorrarCurso'),
    path('curso/<pk>/actualizar', views.CursoUpdateView.as_view(), name='ActualizarCurso'),
    path('curso/agregar', views.CursoCreateView.as_view(), name='AgregarCurso'),
    path('profesor/listar', views.ProfesorListView.as_view(), name='ListarProfesores'),
    path('profesor/<pk>/borrar', views.ProfesorDeleteView.as_view(),name='BorrarProfesor'),
    path('profesor/agregar',views.ProfesorCreateView.as_view(),name='AgregarProfesor'),
    path('profesor/<pk>/confirm_borrar', views.ProfesorDeleteView.as_view(),name='eliminar_profesor')
]