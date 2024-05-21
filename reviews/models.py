from django.db import models
from movies.models import Movies
from django.core.validators import MinValueValidator,MaxValueValidator

class Review(models.Model):
  movie = models.ForeignKey(Movies, on_delete=models.PROTECT,related_name='reviews')
  stars = models.IntegerField(validators=[
    MinValueValidator(0,'Escolha uma nota entre 0 e 5.'),
    MaxValueValidator(5,'Escolha uma nota entre 0 e 5.'),
  ])
  coment = models.TextField(null=True,blank=True)

  def __str__(self):
    return str(self.movie)
