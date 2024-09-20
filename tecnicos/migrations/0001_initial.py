# Generated by Django 5.1.1 on 2024-09-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=30)),
                ('rol', models.CharField(choices=[('tecnico', 'tecnico'), ('asistente', 'asistente'), ('medico', 'medico'), ('preparador fisico', 'preparador fisico')], max_length=40)),
            ],
        ),
    ]
