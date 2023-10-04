# Generated by Django 4.2.5 on 2023-10-04 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0013_alter_review_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
