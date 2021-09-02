from datetime import time, timezone
from django.db import models

# Create your models here.

# --------------------Genres Model--------------------


class Genres(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.type}"

    class Meta:
        verbose_name_plural = 'Genres'
# --------------------Tag Model--------------------


class Tags(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.tag}"

    class Meta:
        verbose_name_plural = 'Tags'
# --------------------Publishers Model--------------------


class Publishers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Publishers'
# --------------------Games Model--------------------


class Games(models.Model):
    tags = models.ManyToManyField(Tags)
    genres = models.ManyToManyField(Genres)
    name = models.CharField(max_length=255)
    esrb = models.CharField(max_length=30)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    matacritics = models.IntegerField()
    description = models.CharField(max_length=5000)
    best_of_all_time = models.BooleanField()
    release_date = models.DateField(auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ['-release_date']
        verbose_name_plural = 'Games'