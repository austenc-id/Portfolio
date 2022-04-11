from django.db.models import Model, AutoField, CharField, TextField, URLField

# Create your models here.


class Base(Model):
    ID = AutoField(primary_key=True)
    label = CharField(max_length=14)

    def __str__(self):
        return f'{self.label}'

class Link(Base):
    url = URLField()
    icon = TextField()


class Story(Base):
    class Meta:
        verbose_name_plural = 'Stories'
    title = CharField(max_length=14)
    content = TextField()
