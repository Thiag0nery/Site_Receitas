# Generated by Django 4.2 on 2023-05-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0008_alter_postreceitas_post_usuario_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreceitas',
            name='post_ingredientes',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_nome',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='postreceitas',
            name='post_preparo',
            field=models.CharField(max_length=50),
        ),
    ]
