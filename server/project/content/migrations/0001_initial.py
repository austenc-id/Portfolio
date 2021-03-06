# Generated by Django 4.0.3 on 2022-04-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('icon', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=14)),
                ('content', models.TextField()),
                ('page_index', models.IntegerField(default=1)),
                ('paragraphs', models.ManyToManyField(related_name='story_paragraphs', to='content.paragraph')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
