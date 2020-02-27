from django.db import models

# Create your models here.

class BlogPost(models.Model):
    # id = models.IntegerField() -> primary key or pk
    title = models.TextField()
    slug = models.SlugField(unique=True) # hello world -> hello-world, you can set a default by using default="value-of-default"
    content = models.TextField(null=True, blank=True)