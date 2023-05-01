# Generated by Django 4.2 on 2023-05-01 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0006_rename_post_receitas_postreceitas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreceitas',
            name='post_foto',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_ingredientes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_nome',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_preparo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_usuario_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
