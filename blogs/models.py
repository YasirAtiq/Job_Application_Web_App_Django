"""Models for the application 'blogs' """
from django.db import models



class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    content = models.TextField(max_length=2450)
    thumbnail_img = models.ImageField(upload_to="blog_thumbnails/",
                                      null=True, blank=True)
    date_created = models.DateField(auto_created=True, null=True)
    
    def __str__(self):
        return f"Blog: {self.title}"



class BlogContentImages(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, 
                             related_name='content_images')
    content_images = models.ImageField(upload_to="blog_content_images/",
                                       null=True, blank=True)