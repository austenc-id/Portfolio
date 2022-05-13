from rest_framework.serializers import HyperlinkedModelSerializer
from .content import Link, Chapter, Story, Paragraph


class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        # fields = ['id', 'url', 'icon']


class ChapterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        # fields = ['id', 'title', 'stories']


class StorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
        # fields = ['id', 'order', 'title', 'paragraphs', 'page_index', 'url']


class ParagraphSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'
        # fields = ['id', 'content']