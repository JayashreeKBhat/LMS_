# Generated by Django 4.1.7 on 2023-05-09 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_video_quizlink_delete_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='quizlink',
            new_name='quiz_id',
        ),
    ]