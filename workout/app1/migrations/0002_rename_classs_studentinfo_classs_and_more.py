# Generated by Django 5.0.1 on 2024-01-09 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Classs',
            new_name='classs',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Name',
            new_name='dep',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='department',
            new_name='name',
        ),
    ]
