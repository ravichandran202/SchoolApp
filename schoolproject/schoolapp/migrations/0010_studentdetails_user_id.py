# Generated by Django 4.1.7 on 2023-12-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0009_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentdetails",
            name="user_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
