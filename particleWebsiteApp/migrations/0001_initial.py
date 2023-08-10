# Generated by Django 4.2.4 on 2023-08-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Particle",
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
                ("name", models.CharField(max_length=20)),
                ("charge", models.FloatField(blank=True, default=0, null=True)),
                ("fundamental", models.CharField(max_length=200)),
                ("summary", models.CharField(max_length=500)),
                ("short_summary", models.CharField(max_length=200)),
                ("fun_fact", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
