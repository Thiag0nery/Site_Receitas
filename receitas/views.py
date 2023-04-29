from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from . import models
class BaseViws(ListView):
    template_name = 'receitas/homepage.html'
    model = models.Post_Receitas
    context_object_name = 'receitas'
