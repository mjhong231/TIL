from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)