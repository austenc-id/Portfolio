from django.db.models import Model, IntegerField, CharField, TextField, URLField, AutoField, ManyToManyField

# Create your models here.

class Link(Model):
    id = AutoField(primary_key=True)
    url = URLField()
    icon = TextField()
    def __str__(self):
        return f'{self.url}'

class Story(Model):
    class Meta:
        verbose_name_plural = 'Stories'
    id = AutoField(primary_key=True)
    order = IntegerField(default=0)
    title = CharField(max_length=14)
    page_index = IntegerField(default=1)
    paragraphs = ManyToManyField('Paragraph', related_name='story_paragraphs')
    def __str__(self):
        return f'{self.title}'
class Paragraph(Model):
    id = AutoField(primary_key=True)
    content=TextField()
    def __str__(self):
        return f'paragraph id:{self.id}'