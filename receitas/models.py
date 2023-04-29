from django.db import models
from django.contrib.auth.models import User
class Post_Receitas(models.Model):
    post_codigo = models.BigAutoField(primary_key=True)
    post_usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    post_foto = models.ImageField(null=True,blank=True)
    post_nome = models.CharField(max_length=80, null=False)
    post_ingretientes = models.CharField(max_length=100, null=False)
    post_preparo = models.CharField(max_length=255, null=False)
