from django.urls import path
from . import views
app_name = 'receitas'
urlpatterns = [
    path('', views.BaseViws.as_view(), name='homepage'),
    path('<post_codigo>',views.Detalhe.as_view(),name='detalhe'),
    path('busca/', views.Busca.as_view(),name='buscar')
]