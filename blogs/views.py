"""The Front-End View of the App 'blogs'"""
from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from .models import Blogs

class BlogList(generic.ListView):
    template_name = "blogs_list.html"
    model = Blogs

    def get_queryset(self):
        return Blogs.objects.order_by("title")