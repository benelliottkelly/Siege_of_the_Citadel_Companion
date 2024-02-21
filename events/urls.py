from django.urls import path
from .views import EventCreateAPIView, EventDetailView

urlpatterns = [
  path('', EventCreateAPIView.as_view()), # /events/
  path('<int:pk>/', EventDetailView.as_view()) #/events/:pk/
]