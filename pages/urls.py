from django.urls import path
from .views import about, home, index

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("pages/", home, name="home"),
]
