from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


class Song(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
