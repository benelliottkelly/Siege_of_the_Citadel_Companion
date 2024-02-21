from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event
from .serializers.common import EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Path: /events/
# Methos: GET, POST
class EventCreateAPIView(ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /events/:pk/
# Methods: GET, PUT, PATCH, DELETE
class EventDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
