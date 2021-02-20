from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin


from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()



# Create your views here.

class MascList(SelectRelatedMixin, generic.ListView):
    model = models.Mascota
    select_related = ("user", "veterinario")



class CreateMascot(LoginRequiredMixin,generic.CreateView):
    fields = ('name','especie','raza','vet_id')
    model = models.Mascota

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
     

class SingleMascot(generic.DetailView):
    model = models.Mascota     