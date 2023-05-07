from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from . import models
from . import forms
class BaseViws(ListView):
    template_name = 'receitas/homepage.html'
    model = models.PostReceitas
    context_object_name = 'receitas'


class Busca(BaseViws):
    def get_queryset(self, *args, **kwargs):
        nome = self.request.GET.get('nome')
        qs = super().get_queryset(*args, **kwargs)
        if not nome:
            return qs
        qs = qs.filter(
            Q(post_nome__icontains=nome)
        )
        return qs
"""
class Categoria(BaseViws):
    template_name = 'receitas/homepage_categoria.html'
    def super(self,request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        categoria = self.kwargs.get('cat_codigo')
        categoria_receita = get_object_or_404(models.PostReceitas, post_categoria_fk=categoria)
        self.contexto = {
            'receitas':categoria_receita,
            'categorias': models.CategoriaModel.objects.all()
        }

        self.pagea = render(self.request,self.template_name,self.contexto)
    def get(self, *args, **kwargs):
        return self.pagea

"""
class Detalhe(DetailView):
    model = models.PostReceitas
    template_name = 'receitas/detalhe.html'
    context_object_name = 'receita'
    pk_url_kwarg = 'post_codigo'
