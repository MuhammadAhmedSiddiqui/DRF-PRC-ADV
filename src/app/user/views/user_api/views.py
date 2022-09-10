from rest_framework.viewsets import ModelViewSet

from user.serializer import UserSerializer
from core import models


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
