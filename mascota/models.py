from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from veterinario.models import Veterinario
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Mascota(models.Model):
    name = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name='mascotas',on_delete=models.CASCADE,null=True)
    vet_id = models.ManyToManyField(Veterinario,through="VetMember")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mascota:single',kwargs={ 'pk':self.pk})
    class Meta:
        ordering = ["name"]


class VetMember(models.Model):
    Mascota = models.ForeignKey(Mascota,related_name='memberships',on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario,related_name='vet_masc',on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("Mascota","veterinario")


