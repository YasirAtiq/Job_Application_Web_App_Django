"""The Front-End View of the App 'blogs'"""
from django.views import generic

class BlogList(generic.ListView):
    template_name = "blogs_list.html"
    model = None