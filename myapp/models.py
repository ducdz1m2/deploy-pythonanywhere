from django.db import models

# Create your models here.
class Game(models.Model):
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    torrent = models.TextField(blank=True)
    mega = models.TextField(blank=True)