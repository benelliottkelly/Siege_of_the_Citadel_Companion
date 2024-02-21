from django.urls import path
from .views import EntrancePointCreateAPIView, EntrancePointDetailView

urlpatterns = [
  path('', EntrancePointCreateAPIView.as_view()), # /entrance_points/
  path('<int:pk>/', EntrancePointDetailView.as_view())
]