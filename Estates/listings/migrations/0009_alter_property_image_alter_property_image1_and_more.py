# Generated by Django 5.1 on 2024-08-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0008_property_approved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="image",
            field=models.ImageField(max_length=300, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="property",
            name="image1",
            field=models.ImageField(max_length=300, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="property",
            name="image2",
            field=models.ImageField(max_length=300, upload_to="images/"),
        ),
    ]
