from .serializers.common import RegistrationSerializer, UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from lib.permissions import IsUserProfileOrReadOnly

User = get_user_model()


# Path: /auth/register/
# Method GET, POST
class RegisterView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegistrationSerializer

# Path: /users/:pk
# Method GET
class UserDetailView(RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsUserProfileOrReadOnly]