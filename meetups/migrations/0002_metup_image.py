# Generated by Django 3.2.7 on 2021-09-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metup',
            name='image',
            field=models.ImageField(default='test', upload_to='image'),
            preserve_default=False,
        ),
    ]
