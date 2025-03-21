# Generated by Django 5.1.7 on 2025-03-17 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('adresse_postale', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Faculte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('couleur', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_de_naissance', models.DateField()),
                ('matricule', models.CharField(max_length=10, unique=True)),
                ('courriel', models.EmailField(max_length=254, unique=True)),
                ('tel_fixe', models.CharField(blank=True, max_length=20, null=True)),
                ('tel_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('mot_de_passe', models.CharField(max_length=32)),
                ('amis', models.ManyToManyField(blank=True, to='DjangoProject9.personne')),
                ('faculte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnes', to='DjangoProject9.faculte')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_de_publication', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='DjangoProject9.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DjangoProject9.personne')),
                ('bureau', models.CharField(max_length=30)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employes', to='DjangoProject9.campus')),
                ('fonction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employes', to='DjangoProject9.fonction')),
            ],
            bases=('DjangoProject9.personne',),
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DjangoProject9.personne')),
                ('annee', models.IntegerField()),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etudiants', to='DjangoProject9.cursus')),
            ],
            bases=('DjangoProject9.personne',),
        ),
    ]
