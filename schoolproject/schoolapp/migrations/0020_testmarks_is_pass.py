# Generated by Django 4.1.7 on 2023-12-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0019_alter_testmarks_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="testmarks",
            name="is_pass",
            field=models.BooleanField(default=False),
        ),
    ]