from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^personalSalud/', views.personalSaludList),
    url(r'^personalSaludCreate/$', csrf_exempt(views.personalSaludCreate), name='personalSaludCreate'),
]