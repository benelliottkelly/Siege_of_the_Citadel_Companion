from django.urls import path
from .views import DarkLegionCreateAPIView, DarkLegionDetailView

urlpatterns = [
  path('', DarkLegionCreateAPIView.as_view()), # /dark_legion/
  path('<int:pk>/', DarkLegionDetailView.as_view()) # /dark_legion/:pk
]