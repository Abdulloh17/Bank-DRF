from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer, UserRegisterSerializer, User

class UserApiViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action in ('create' ):
            return UserRegisterSerializer
        return UserSerializer
