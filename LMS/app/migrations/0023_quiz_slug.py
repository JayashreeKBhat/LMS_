# Generated by Django 4.1.7 on 2023-05-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0022_remove_learnout_course_learnout_lesson"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="slug",
            field=models.SlugField(blank=True, default="", max_length=500, null=True),
        ),
    ]
