# Generated by Django 3.2.7 on 2023-06-08 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsLetter', '0008_auto_20230608_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='Intensity',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='Likehood',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='Relevance',
        ),
    ]
