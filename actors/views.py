from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class ActorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


