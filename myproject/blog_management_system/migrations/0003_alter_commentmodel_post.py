# Generated by Django 5.1.6 on 2025-02-08 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_management_system', '0002_rename_category_blogpostmodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_management_system.blogpostmodel'),
        ),
    ]
