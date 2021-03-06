# Generated by Django 3.1.7 on 2021-03-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galerie', models.CharField(choices=[('A', 'App'), ('M', 'Meeting'), ('O', 'Autre')], max_length=1)),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='Titre')),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Galerie',
            },
        ),
    ]
