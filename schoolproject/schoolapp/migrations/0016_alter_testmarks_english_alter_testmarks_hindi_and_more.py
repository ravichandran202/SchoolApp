# Generated by Django 4.1.7 on 2023-12-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolapp", "0015_testmarks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testmarks", name="english", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks", name="hindi", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks", name="kannada", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks", name="maths", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks", name="science", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks", name="social", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="testmarks",
            name="total_marks",
            field=models.FloatField(default=0),
        ),
    ]