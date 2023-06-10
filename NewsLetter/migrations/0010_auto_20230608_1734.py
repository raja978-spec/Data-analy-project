# Generated by Django 3.2.7 on 2023-06-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsLetter', '0009_auto_20230608_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='Intensity',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Likehood',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Relevance',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='Country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='Region',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='Topic',
            field=models.CharField(default='', max_length=100),
        ),
    ]
