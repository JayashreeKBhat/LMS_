# Generated by Django 4.1.7 on 2023-04-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_language_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Certificate',
            field=models.BooleanField(default=False, null=True),
        ),
    ]