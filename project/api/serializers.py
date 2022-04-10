from django.contrib.auth.models import User, Group
from stories.models import Story
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
        fields = ['url', 'label', 'title', 'content']
