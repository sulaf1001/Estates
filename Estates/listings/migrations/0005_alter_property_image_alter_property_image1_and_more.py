# Generated by Django 5.1 on 2024-08-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0004_alter_property_image_alter_property_image1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="property",
            name="image1",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="property",
            name="image2",
            field=models.ImageField(upload_to="images"),
        ),
    ]
