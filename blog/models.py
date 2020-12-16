from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE # SET_NULL, PROTECT
    )

    posted_at = models.DateTimeField(auto_now_add=True) # Created
    modified_at = models.DateTimeField(auto_now=True) # Last modified

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images')
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            '-posted_at',
        )
    
