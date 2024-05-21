from rest_framework import serializers
from movies.models import Movies
from reviews.models import Review
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer

class MoviesSerializer(serializers.ModelSerializer):
  
  
  
  class Meta:
    model = Movies
    fields = '__all__'

  

  def validate_release_date(self,value):
    if value.year > 2024:
      raise serializers.ValidationError('So e possivel adicional filmes ate o ano atual')
    return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    def get_rate(self,obj):
      rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

      if rate:
        return round(rate,1)

      return None

    class Meta:
        model = Movies
        fields = ['id', 'title', 'genre', 'actors' , 'release_date', 'rate', 'resume']
