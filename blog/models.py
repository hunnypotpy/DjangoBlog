from django.db import models
from django.conf import settings

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    post = models.TextField()
    slug = models.SlugField(max_length=50)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-added']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank = True, null=True)
    # TODO: upload image to cloud / S3
    url = models.URLField(blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.url:
            # then it's on S3
            return self.url
        # it's local
        return self.image.url

#corey

'''from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title'''

