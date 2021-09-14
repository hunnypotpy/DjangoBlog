from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    post = models.TextField()
    slug = models.SlugField(max_length=50)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-added']


