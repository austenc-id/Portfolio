# Generated by Django 4.0.3 on 2022-04-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
