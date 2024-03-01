from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
    else:
      return request.user == obj.owner
    
class IsUserProfileOrReadOnly(BasePermission):
  def has_object_permission(self, request, view, obj):
    # Uncomment below and indent return to allow authorized users to view other users
    # if request.method in SAFE_METHODS:
    #   return True
    # else:
    return request.user.id == obj.pk