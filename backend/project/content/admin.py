from django.contrib import admin
from .models import (
    Link,
    Chapter,
    Story,
    Paragraph
)
# Register your models here.

admin.site.register(Link)
admin.site.register(Chapter)
admin.site.register(Story)
admin.site.register(Paragraph)
