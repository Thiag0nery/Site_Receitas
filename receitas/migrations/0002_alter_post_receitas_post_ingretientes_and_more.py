# Generated by Django 4.2 on 2023-04-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_receitas',
            name='post_ingretientes',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post_receitas',
            name='post_preparo',
            field=models.TextField(max_length=255),
        ),
    ]
