# Generated by Django 4.1.3 on 2023-01-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Docente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=30)),
                ("Apellido_Paterno", models.CharField(max_length=20)),
                ("Apellido_Materno", models.CharField(max_length=20)),
                ("DNI", models.CharField(max_length=8)),
                ("Fecha_Nacimiento", models.DateField()),
                ("Fecha_Registro", models.DateTimeField(auto_now_add=True)),
                ("Estado", models.CharField(max_length=15)),
            ],
        ),
    ]
