# Generated by Django 4.0.3 on 2022-04-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_link_link_id_story_group_story_story_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='group',
            field=models.CharField(max_length=14),
        ),
    ]
