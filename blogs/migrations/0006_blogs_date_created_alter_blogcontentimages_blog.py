# Generated by Django 4.2.6 on 2023-12-01 14:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0005_alter_blogs_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogs",
            name="date_created",
            field=models.DateField(
                auto_created=True,
                default=datetime.datetime(
                    year=2023, month=12, day=1, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blogcontentimages",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content_images",
                to="blogs.blogs",
            ),
        ),
    ]
