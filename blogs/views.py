"""The Front-End View of the App 'blogs'"""
from django.views import generic
from .models import Blogs


class BlogListView(generic.ListView):
    template_name = "blogs_list.html"
    model = Blogs

    def get_queryset(self):
        return Blogs.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blogs.objects.all()
        return context


class BlogDetailView(generic.DetailView):
    template_name = "blog.html"
    model = Blogs
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        context['images'] = blog.content_images.all()
        return context