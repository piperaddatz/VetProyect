from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from veterinario.models import Veterinario
from . import models

from braces.views import SelectRelatedMixin 
# Create your views here.

class CreateVet(LoginRequiredMixin,generic.CreateView):
    fields = ('vet_name','direction')
    model = models.Veterinario

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class SingleVet(generic.DetailView):
    model = Veterinario


class ListVet(generic.ListView):
    model = Veterinario     


   

class DeleteVet(generic.DeleteView):
    model = Veterinario
    success_url = reverse_lazy("veterinario:all")





            
class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("veterinario:single",kwargs={"pk": self.kwargs.get("pk")})

    def get(self, request, *args, **kwargs):
        Veterinario = get_object_or_404(Veterinario,pk=self.kwargs.get("pk"))

        try:
            VetMember.objects.create(user=self.request.user,Veterinario=Veterinario)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(Veterinario.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(Veterinario.name))

        return super().get(request, *args, **kwargs)
        
