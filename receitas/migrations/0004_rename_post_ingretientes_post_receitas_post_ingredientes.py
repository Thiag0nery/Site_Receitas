# Generated by Django 4.2 on 2023-04-30 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_alter_post_receitas_post_ingretientes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_receitas',
            old_name='post_ingretientes',
            new_name='post_ingredientes',
        ),
    ]
