# Generated by Django 3.2.9 on 2022-03-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_alter_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
