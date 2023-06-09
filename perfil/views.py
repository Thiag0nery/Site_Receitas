from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from . import forms
from django.views import View
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

class BaseViews(View):
    templates_name = 'perfil/index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        self.contexto = {
            'usuario': forms.UserForms(
                data=self.request.POST or None
            ),
            'formulario': forms.Formulario(
                data=self.request.POST or None
            ),
        }

        self.usuario = self.contexto['usuario']
        self.publicarReceita = self.contexto['formulario']
        self.page = render(self.request, self.templates_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.page
class Login(BaseViews):
    templates_name = 'perfil/index.html'
    def post(self, *args,  **kwargs):
        usuario = self.request.POST.get('username')
        senha = self.request.POST.get('password')

        user = authenticate(
            self.request, username=usuario, password=senha)
        print(bool(user))
        if not user:
            messages.error(
             self.request,
                "Usuario ou Senha incorretos"
            )
            return self.page
        login(self.request, user=user)
        messages.success(
            self.request,
            "Login efetuado com sucesso"
        )
        return redirect('receitas:homepage')
class Cadastro(BaseViews):
    templates_name = 'perfil/cadastro.html'
    def post(self, *args,  **kwargs):
        if not self.usuario.is_valid():
            messages.error(
                self.request,
                self.usuario.errors
            )

            return self.page

        senha = self.request.POST.get('password')
        usuario = self.usuario.save(commit=False)
        usuario.set_password(senha)
        usuario.save()

        return redirect('perfil:login')

class PublicarReceita(BaseViews):
    templates_name = 'receitas/publicar.html'

    def post(self, *args,  **kwargs):
        if not self.publicarReceita.is_valid() :
            messages.error(
                self.request,
                self.publicarReceita.errors
            )

            return self.page
        if self.request.FILES.get('post_foto') == None :

            messages.error(
                self.request,
                "Este campo é obrigatório"
            )

            return self.page

        self.foto = self.request.FILES.get('post_foto')
        self.idUsuario = get_object_or_404(User, username=self.request.user)
        receita = self.publicarReceita.save(commit=False)
        receita.post_foto = self.foto
        receita.post_usuario_fk = self.idUsuario
        receita.save()

        messages.success(
            self.request,
            'A sua receita foi enviada para equipe de aprovação.'
        )

        return redirect('receitas:homepage')
class Logout(View):
    def get(self, *args, **kwargs):


        logout(self.request)


        return redirect('perfil:login')