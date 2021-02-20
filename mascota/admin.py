from django.contrib import admin
from . import models

# Register your models here.

class VetMemberInLine(admin.TabularInline):
    model = models.VetMember
    

admin.site.register(models.Mascota)