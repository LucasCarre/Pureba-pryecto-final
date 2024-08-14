from django import forms

class Alumno_formulario(forms.Form):
    nombre = forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    
class Profesor_formulario(forms.Form):
    nombre = forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    
class Buscar_cursos(forms.Form):
    curso = forms.CharField()
