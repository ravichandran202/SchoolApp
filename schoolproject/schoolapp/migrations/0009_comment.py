# Generated by Django 4.1.7 on 2023-12-16 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("schoolapp", "0008_announcement_announce_to"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField()),
                (
                    "announcement_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schoolapp.announcement",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("schoolapp.basicinfo",),
        ),
    ]
