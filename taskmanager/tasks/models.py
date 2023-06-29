from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=2000)
    img = models.TextField(max_length=1000)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    changed_at = models.DateTimeField(auto_now=True, auto_created=True)


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-created_at']

    def __str__(self):
        return self.title