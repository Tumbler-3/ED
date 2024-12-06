# Generated by Django 5.1.3 on 2024-12-05 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_alter_postmodel_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
    ]
