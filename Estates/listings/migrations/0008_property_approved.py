# Generated by Django 5.1 on 2024-08-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0007_alter_property_image_alter_property_image1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
