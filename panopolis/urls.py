from django.urls import path
from panopolis import views

app_name = 'panopolis'

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("about/", views.about, name="about"),
]

