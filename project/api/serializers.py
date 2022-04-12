from django.contrib.auth.models import User, Group
from content.models import Link, Story, Paragraph
from rest_framework.serializers import HyperlinkedModelSerializer


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
        fields = ['link_id', 'label', 'url', 'icon']

class StorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['story_id', 'label', 'title', 'content', 'paragraphs', 'page_index', 'url']

class ParagraphSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['paragraph_id', 'label', 'content']
