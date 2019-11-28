# Generated by Django 2.2.7 on 2019-11-28 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrera',
            old_name='usuario',
            new_name='director',
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='correo',
        ),
        migrations.AddField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]