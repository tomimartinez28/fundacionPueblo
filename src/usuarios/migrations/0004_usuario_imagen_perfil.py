# Generated by Django 4.0.6 on 2022-08-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_es_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_perfil'),
        ),
    ]
