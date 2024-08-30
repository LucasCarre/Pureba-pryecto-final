from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='Appyeri/inicio.html'), name="Logout"),
    path('editar_usuario/', views.editar_usuario, name='EditarUsuario'),
    path('camabiar_password/', views.CambiarPasswordView.as_view(), name='CambiarContra')
]