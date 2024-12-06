# Generated by Django 5.1.3 on 2024-12-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='updated_at'),
        ),
    ]
