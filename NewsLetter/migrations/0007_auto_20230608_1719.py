# Generated by Django 3.2.7 on 2023-06-08 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsLetter', '0006_auto_20230608_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='EYear',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='SYear',
        ),
    ]
