# Generated by Django 4.1.7 on 2023-03-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='I never added the description...', max_length=200),
        ),
    ]
