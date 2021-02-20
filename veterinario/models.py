from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()


from django.urls import reverse
from django import template
register = template.Library()

import misaka


class Veterinario(models.Model):

    vet_name = models.CharField(max_length=264, unique=True)
    direction = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.vet_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("veterinario:single", kwargs={ 'pk':self.pk})


    class Meta:
        ordering = ["vet_name"]

# Create your models here.

