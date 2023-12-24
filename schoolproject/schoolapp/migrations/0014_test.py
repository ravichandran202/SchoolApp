# Generated by Django 4.1.7 on 2023-12-24 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0013_alter_studentdetails_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "basicinfo_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="schoolapp.basicinfo",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("test_for", models.IntegerField()),
                ("description", models.TextField()),
            ],
            bases=("schoolapp.basicinfo",),
        ),
    ]