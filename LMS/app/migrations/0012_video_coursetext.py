# Generated by Django 4.1.7 on 2023-04-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='courseText',
            field=models.FileField(default=1, max_length=254, upload_to=None),
            preserve_default=False,
        ),
    ]
