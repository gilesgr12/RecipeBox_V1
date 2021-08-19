from django.db import models
from django.contrib.auth.models import User


# Create your models here.
"""
Author:
- name
- byline (optional)
Recipe:
- Body
- Author
- post_created
- Title
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    ingredients = models.TextField()
    time_required = models.TextField()
    directions = models.TextField()

    def __str__(self):
        return self.title
