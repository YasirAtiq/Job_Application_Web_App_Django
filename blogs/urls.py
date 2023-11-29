"""URL Configuration for application: "blogs" """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogs_list"),
]