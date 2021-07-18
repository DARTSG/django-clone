# Generated by Django 3.2.5 on 2021-07-17 20:26

import django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sample", "0018_auto_20210628_2301"),
    ]

    operations = (
        [
            migrations.AddConstraint(
                model_name="saletag",
                constraint=models.UniqueConstraint(
                    fields=("name",), name="sale_tag_unique_name"
                ),
            ),
        ]
        if django.VERSION >= (2, 2)
        else [
            migrations.AlterField(
                model_name="saletag",
                name="name",
                field=models.CharField(max_length=255, unique=True),
            ),
        ]
    )
