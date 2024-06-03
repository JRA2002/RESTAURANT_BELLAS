# Generated by Django 5.0.6 on 2024-06-03 17:35

import inventory.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0049_alter_ingredient_unit"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ing_Category",
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
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="ingredient",
            name="category",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name=inventory.models.Ing_Category,
            ),
        ),
    ]
