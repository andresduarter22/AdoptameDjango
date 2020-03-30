# Generated by Django 3.0.4 on 2020-03-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200328_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='age',
        ),
        migrations.AlterField(
            model_name='animal',
            name='race',
            field=models.CharField(choices=[('d', 'dog'), ('c', 'cat'), ('o', 'other')], max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='size',
            field=models.CharField(choices=[('s', 'short'), ('m', 'medium'), ('b', 'big')], max_length=200),
        ),
    ]
