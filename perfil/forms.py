from django import forms
from django.contrib.auth.models import User
from receitas.models import PostReceitas

class UserForms(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
    class Meta:
        model = User
        fields = ('username','password','email','password2')
    def clean(self):
        username_form = self.cleaned_data.get('username')
        password_form = self.cleaned_data.get('password')
        email_form = self.cleaned_data.get('email')
        password2_form = self.cleaned_data.get('password2')

        validation_error_msgs = {}



        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_password_match = 'As duas senhas não conferem'
        error_msg_required_field = 'Este campo é obrigatório.'

        usuario_banco = User.objects.filter(username=username_form).first()
        email_banco =  User.objects.filter(email=email_form).first()

        print(usuario_banco)

        if usuario_banco:
            validation_error_msgs['username'] = error_msg_user_exists

        if email_banco:
            validation_error_msgs['email'] = error_msg_email_exists

        if not password_form:
            validation_error_msgs['password'] = error_msg_required_field

        if not password2_form:
            validation_error_msgs['password2'] = error_msg_required_field

        if password_form != password2_form:
            validation_error_msgs['password'] = error_msg_password_match
            validation_error_msgs['password2'] = error_msg_password_match


        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
class Formulario(forms.ModelForm):
    class Meta:
        model = PostReceitas
        fields = '__all__'

    def clean(self):
        nome_receita = self.cleaned_data.get('post_nome')
        receita_ingredientes = self.cleaned_data.get('post_ingredientes')
        preparo_receita = self.cleaned_data.get('post_preparo')

        validation_error_msgs = {}

        error_msg_required_field = 'Este campo é obrigatório.'



        if not nome_receita:
            validation_error_msgs['post_nome'] = error_msg_required_field



        if not receita_ingredientes:
            validation_error_msgs['post_ingredientes'] = error_msg_required_field

        if not preparo_receita:
            validation_error_msgs['post_preparo'] = error_msg_required_field

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))