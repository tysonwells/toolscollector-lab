# Generated by Django 3.2.9 on 2021-12-01 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_tool_modelnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='modelNum',
            new_name='modelNumber',
        ),
    ]
