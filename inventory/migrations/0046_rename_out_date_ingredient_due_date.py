# Generated by Django 5.0.6 on 2024-06-02 14:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0045_provider_rename_kanban_ingredient_reorder_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ingredient",
            old_name="out_date",
            new_name="due_date",
        ),
    ]