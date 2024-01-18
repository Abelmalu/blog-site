from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(default='defaultProfile.png')

    def __str__(self) -> str:
        return str(self.user)


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author =models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    person = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    #add in author later
    def __str__(self) -> str:
        return self.title
    def snippet(self):
        return self.body[:100]+'....'
    

