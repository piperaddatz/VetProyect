from django import forms

from mascota import models


class MascotForm(forms.ModelForm):
    class Meta:
        fields = ('name','especie','raza','vet_id')
        model = models.Mascota

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["Veterinario"].queryset = (
                models.Veterinario.objects.filter(
                    pk__in=user.veterinario.values_list("veterinario__pk")
                )
            )



