# Generated by Django 2.2.3 on 2019-08-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20190730_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='blob',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blob',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
