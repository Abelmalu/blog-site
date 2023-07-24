from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug =models.SlugField()
    body =models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author =models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    #add in author later
    def __str__(self) -> str:
        return self.title
    def snippet(self):
        return self.body[:50]+'....'