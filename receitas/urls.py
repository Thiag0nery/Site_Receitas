from django.urls import path
from . import views
app_name = 'receitas'
urlpatterns = [
    path('', views.BaseViws.as_view(), name='homepage')
]