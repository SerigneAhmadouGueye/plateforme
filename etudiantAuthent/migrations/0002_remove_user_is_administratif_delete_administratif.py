# Generated by Django 4.2.3 on 2023-08-16 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiantAuthent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_Administratif',
        ),
        migrations.DeleteModel(
            name='Administratif',
        ),
    ]
