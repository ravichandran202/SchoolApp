# Generated by Django 4.1.7 on 2023-12-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0016_alter_testmarks_english_alter_testmarks_hindi_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="testmarks", old_name="total_marks", new_name="scored_marks",
        ),
        migrations.AddField(
            model_name="test", name="total_marks", field=models.IntegerField(default=0),
        ),
    ]
