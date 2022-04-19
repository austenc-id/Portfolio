from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from content.serializers import (
    UserSerializer,
    GroupSerializer,
    LinkSerializer,
    ChapterSerializer,
    StorySerializer,
    ParagraphSerializer
)
from content.models import (
    Link,
    Chapter,
    Story,
    Paragraph)
# Create your views here.


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthenticated
    ]


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all().order_by(('id'))
    serializer_class = LinkSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]


class ChapterViewSet(ModelViewSet):
    queryset = Chapter.objects.all().order_by('id')
    serializer_class = ChapterSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]


class StoryViewSet(ModelViewSet):
    """
    API endpoint that allows Stories to be viewed or edited.
    """
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]


class ParagraphViewSet(ModelViewSet):
    queryset = Paragraph.objects.all().order_by('id')
    serializer_class = ParagraphSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]
