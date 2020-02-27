from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField() -> primary key or pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #you can also use models.CASCADE
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) # hello world -> hello-world, you can set a default by using default="value-of-default"
    content = models.TextField(null=True, blank=True)