from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'veterinario'

urlpatterns = [
    url(r"^$", views.ListVet.as_view(), name="all"),
    url(r"^new/$", views.CreateVet.as_view(), name="create"),
    url(r"mascota/by/(?P<pk>\d+)/$",views.SingleVet.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteVet.as_view(),name="delete"),
]