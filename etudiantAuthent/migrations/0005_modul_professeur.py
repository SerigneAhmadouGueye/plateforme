# Generated by Django 4.2.3 on 2023-08-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiantAuthent', '0004_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modul', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('tel', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
            ],
        ),
    ]