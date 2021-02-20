# Generated by Django 3.1.4 on 2021-02-16 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veterinario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('especie', models.CharField(max_length=255, unique=True)),
                ('raza', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VetMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='mascota.mascota')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_masc', to=settings.AUTH_USER_MODEL)),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vet_masc', to='veterinario.veterinario')),
            ],
            options={
                'unique_together': {('mascota', 'user')},
            },
        ),
        migrations.AddField(
            model_name='mascota',
            name='user_id',
            field=models.ManyToManyField(through='mascota.VetMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mascota',
            name='vet_id',
            field=models.ManyToManyField(through='mascota.VetMember', to='veterinario.Veterinario'),
        ),
    ]
