from django.db import models
from djnago.utils import timezone

# Create your models here.
class Post(models.Model):
    """ Модель данных для поста блога attr: title, slug, body"""
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISH = 'PB', 'Publish'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title