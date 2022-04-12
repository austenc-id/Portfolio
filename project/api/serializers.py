from django.contrib.auth.models import User, Group
from content.models import Story, Link
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['story_id', 'label', 'title', 'content', 'paragraphs', 'page_index', 'url']

class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['link_id', 'label', 'url', 'icon']
