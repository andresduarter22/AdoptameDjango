# Generated by Django 3.0.4 on 2020-03-31 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200330_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='picture',
            field=models.FileField(default='main/static/media/animal/rey.png', upload_to='animal/'),
        ),
    ]
