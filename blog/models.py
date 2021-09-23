from django.db import models
from django.conf import settings

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    post = models.TextField()
    slug = models.SlugField(max_length=50)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=0)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-added']


