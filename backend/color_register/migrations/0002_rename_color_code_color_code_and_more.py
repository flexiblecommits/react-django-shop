# Generated by Django 4.2.3 on 2023-08-14 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('color_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='color_name',
            new_name='name',
        ),
    ]
