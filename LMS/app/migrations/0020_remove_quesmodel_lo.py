# Generated by Django 4.1.7 on 2023-05-21 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0019_remove_quesmodel_questionid_remove_video_quiz_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="quesmodel", name="lo",),
    ]
