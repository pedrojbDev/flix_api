from rest_framework import generics,views,response,status
from movies.models import Movies
from movies.serializers import MoviesSerializer,MovieListDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.db.models import Count,Avg
from reviews.models import Review


class MoveisCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movies.objects.all()
  
    def get_serializer_class(self):
        if self.request.method == 'GET':
          return MovieListDetailSerializer
        return MoviesSerializer


class MoviesDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movies.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
          return MovieListDetailSerializer
        return MoviesSerializer
    


class MoviesStats(views.APIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movies.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.all().count()
        avarage_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_movies':total_movies,
            'movies_by_genre':movies_by_genre,
            'total_reviews':total_reviews,
            'avarage_stars': round(avarage_stars,1) if avarage_stars else 0,
          },status=status.HTTP_200_OK)