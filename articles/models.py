from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)