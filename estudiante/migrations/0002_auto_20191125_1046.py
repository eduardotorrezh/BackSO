# Generated by Django 2.2.7 on 2019-11-25 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='Carrera',
            new_name='carrera',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='Edad',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='Sexo',
            new_name='sexo',
        ),
    ]