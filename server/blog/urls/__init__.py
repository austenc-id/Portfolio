from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LinkViewSet,
    ChapterViewSet,
    StoryViewSet,
    ParagraphViewSet
)

router = DefaultRouter()
router.register(r'links',
                LinkViewSet)
router.register(r'chapters',
                ChapterViewSet)
router.register(r'stories',
                StoryViewSet)
router.register(r'paragraphs',
                ParagraphViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]