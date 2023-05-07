from django.db import models
from django.contrib.auth.models import User
class CategoriaModel(models.Model):
    cat_codigo = models.BigAutoField(primary_key=True)
    cat_nome = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.cat_nome


class PostReceitas(models.Model):
    post_codigo = models.BigAutoField(primary_key=True,verbose_name='Codigo')
    post_usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name='Usuario')
    post_categoria_fk = models.ForeignKey(CategoriaModel, on_delete=models.DO_NOTHING,blank=True, null=True)
    post_foto = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    post_nome = models.CharField(max_length=80, blank=True,null=True, verbose_name='Nome da receita')
    post_tempo = models.IntegerField(null=True)
    post_ingredientes = models.TextField(max_length=1000, blank=True,null=True)
    post_preparo = models.TextField(max_length=1000, blank=True,null=True)
    post_publicado = models.BooleanField(default=False, verbose_name='Publicado')

