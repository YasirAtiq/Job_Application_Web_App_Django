"""URL Configuration for application: "blogs" """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogList.as_view(), name="blogs_list"),
]