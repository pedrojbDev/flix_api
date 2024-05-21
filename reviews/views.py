from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ReviewCreateList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ReviewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
