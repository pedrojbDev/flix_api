from django.urls import path
from . import views

urlpatterns = [

    path('movies/',views.MoveisCreateListView.as_view(),name='movies-create-list'),
    path('movies/<int:pk>/',views.MoviesDeleteUpdate.as_view(),name='movies-update-delete'),
    path('movies/stats/',views.MoviesStats.as_view(),name='movies-stats')

]