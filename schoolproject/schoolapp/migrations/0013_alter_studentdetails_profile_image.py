# Generated by Django 4.1.7 on 2023-12-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0012_alter_message_receiverid_alter_message_senderid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentdetails",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/profile"),
        ),
    ]