from django.urls import path
from . import views
app_name = 'perfil'
urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('publicara/', views.PublicarReceita.as_view(), name='publicar'),
]