from django.urls import path
from .views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
  path('register/', RegisterView.as_view()), # /api/auth/register/
  path('login/', TokenObtainPairView.as_view()), #/api/auth/login/
  path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), # /api/auth/users/:pk
]