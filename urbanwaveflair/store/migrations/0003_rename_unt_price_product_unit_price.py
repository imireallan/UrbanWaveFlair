# Generated by Django 4.2.5 on 2023-09-25 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_customer_store_custo_first_n_8f83e0_idx"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="unt_price",
            new_name="unit_price",
        ),
    ]