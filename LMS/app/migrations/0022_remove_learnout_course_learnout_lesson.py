# Generated by Django 4.1.7 on 2023-05-21 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0021_learnout_quesmodel_learnout"),
    ]

    operations = [
        migrations.RemoveField(model_name="learnout", name="course",),
        migrations.AddField(
            model_name="learnout",
            name="lesson",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.lesson"
            ),
        ),
    ]
