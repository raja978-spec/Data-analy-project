# Generated by Django 3.2.7 on 2023-06-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsLetter', '0005_auto_20230608_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='Added',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Insight',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Published',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
