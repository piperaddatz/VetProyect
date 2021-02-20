# Generated by Django 3.1.4 on 2021-02-19 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veterinario', '0001_initial'),
        ('mascota', '0002_auto_20210219_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='user_id',
        ),
        migrations.AddField(
            model_name='mascota',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='vetmember',
            unique_together={('mascota', 'veterinario')},
        ),
        migrations.RemoveField(
            model_name='vetmember',
            name='user',
        ),
    ]
