# Generated by Django 3.1.3 on 2020-11-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201119_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mugshot',
            field=models.ImageField(default='static/imgs/dummy_avatar.jpg', upload_to='static/imgs/profile/'),
        ),
    ]
