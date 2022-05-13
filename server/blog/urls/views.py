from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from blog.models import (
    Link,
    Chapter,
    Story,
    Paragraph,
    LinkSerializer,
    ChapterSerializer,
    StorySerializer,
    ParagraphSerializer
    )
# Create your views here.


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