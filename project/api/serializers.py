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
        fields = ['label', 'title', 'content','url']

class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['label', 'url', 'icon']
