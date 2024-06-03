# Generated by Django 5.0.6 on 2024-06-02 12:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0044_menuitem_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Provider",
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
                ("phone", models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name="ingredient",
            old_name="kanban",
            new_name="reorder",
        ),
        migrations.RenameField(
            model_name="ingredient",
            old_name="re_order",
            new_name="reorder_qty",
        ),
        migrations.AddField(
            model_name="ingredient",
            name="out_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="unit_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="ingredient",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="inventory.provider",
            ),
        ),
    ]