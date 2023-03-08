from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="vsd-home"),
]
