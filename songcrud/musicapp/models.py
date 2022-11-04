from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()

    def _str_(self) :
        return self.first_name +' '+ self.last_name

class Song(models.Model):
    title = models.Charfield(max_length=10)
    date_released = models.CharField(max_length=10)
    likes = models.CharField(max_length=10)
    artiste_id = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE,)

    def _str_(self):
        return self.title

class Lyrics(models.Model):
    content = models.CharField(max_length=10)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE,)

    def _str_(self) :
        return self.content