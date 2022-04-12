from django.db.models import Model, IntegerField, CharField, TextField, URLField, AutoField

# Create your models here.


class Base(Model):
    ID = AutoField(primary_key=True)
    label = CharField(max_length=14)

    def __str__(self):
        return f'{self.label}'

class Link(Base):
    link_id = IntegerField(default=0)
    url = URLField()
    icon = TextField()

class Story(Base):
    class Meta:
        verbose_name_plural = 'Stories'
    story_id = IntegerField(default=0)
    title = CharField(max_length=14)
    content = TextField()
    page_index = IntegerField(default=1)
