# Generated by Django 4.1.7 on 2023-12-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "schoolapp",
            "0003_rename_emergency_contact_contact_studentdetails_emergency_contact_number_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BasicInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="studentdetails",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile"),
        ),
    ]