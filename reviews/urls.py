from django.urls import path
from . import views

urlpatterns = [

    path('reviews/',views.ReviewCreateList.as_view(),name='review-create-list'),
    path('reviews/<int:pk>/',views.ReviewUpdateDelete.as_view(),name='review-update-delete'),

]