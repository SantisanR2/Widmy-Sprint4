from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^personalSalud$', views.personalSalud, name='personalSalud'),
]