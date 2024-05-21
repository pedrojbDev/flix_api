from django.db import models
from genres.models import Genre
from actors.models import Actors

class Movies(models.Model):
  title = models.CharField(max_length=100)
  genre = models.ForeignKey(Genre,on_delete=models.PROTECT,related_name='movies')
  release_date = models.DateField(null=True,blank=True)
  actors = models.ManyToManyField(Actors,related_name='movies')
  resume = models.TextField(blank=True,null=True)

  def __str__(self):
    return self.title

  

