from django.contrib import admin
from . import models
class requisicaoReceita(admin.ModelAdmin):
    list_display = ('post_codigo', 'post_nome', 'post_usuario_fk', 'post_publicado',)
    list_editable = ('post_publicado',)
admin.site.register(models.PostReceitas,requisicaoReceita   )
admin.site.register(models.CategoriaModel)
# Register your models here.
