# Generated by Django 4.2 on 2023-05-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0014_postreceitas_post_tempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreceitas',
            name='post_tempo',
            field=models.IntegerField(null=True),
        ),
    ]
