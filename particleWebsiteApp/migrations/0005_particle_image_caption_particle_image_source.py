# Generated by Django 4.2.4 on 2023-08-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("particleWebsiteApp", "0004_alter_particle_charge"),
    ]

    operations = [
        migrations.AddField(
            model_name="particle",
            name="image_caption",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="particle",
            name="image_source",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
