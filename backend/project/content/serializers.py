from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Link, Chapter, Story, Paragraph


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'icon']


class ChapterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'stories']


class StorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'order', 'title', 'paragraphs', 'page_index', 'url']


class ParagraphSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'content']
