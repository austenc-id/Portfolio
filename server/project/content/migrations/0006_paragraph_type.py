# Generated by Django 4.0.3 on 2022-04-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_chapter_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='type',
            field=models.TextField(choices=[('paragraph', 'paragraph'), ('list', 'list')], default='paragraph'),
            preserve_default=False,
        ),
    ]
