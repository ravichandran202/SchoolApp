# Generated by Django 4.1.7 on 2023-12-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0017_rename_total_marks_testmarks_scored_marks_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="testmarks", name="scored_marks",),
        migrations.AddField(
            model_name="testmarks",
            name="total_scored_marks",
            field=models.FloatField(default=0),
        ),
    ]
