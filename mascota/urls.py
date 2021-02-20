from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth import views as auth_views
from . import views 

app_name='mascota'

urlpatterns = [
    url(r"^$", views.MascList.as_view(), name="all"),
    url(r"new/$", views.CreateMascot.as_view(), name="create"),
    url(r"by/(?P<pk>\d+)/$",views.SingleMascot.as_view(),name="single"),
]
