from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class RickAndMortyCharacter(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    origin = models.ForeignKey("Origin", on_delete=models.PROTECT, null=True)
    created = models.DateTimeField()


class Origin(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(verbose_name="origin")
