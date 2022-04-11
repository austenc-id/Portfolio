from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .serializers import (UserSerializer,
                          GroupSerializer,
                          StorySerializer)
from content.models import Story
# Create your views here.


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class StoryViewSet(ModelViewSet):
    """
    API endpoint that allows Stories to be viewed or edited.
    """
    queryset = Story.objects.all().order_by('ID')
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
