# Generated by Django 4.0.6 on 2022-08-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_categoria_modalidad_alter_evento_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
