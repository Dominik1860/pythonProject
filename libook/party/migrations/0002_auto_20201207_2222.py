# Generated by Django 3.1.3 on 2020-12-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='feed',
        ),
        migrations.AlterField(
            model_name='party',
            name='image',
            field=models.ImageField(default='static/imgs/dummy_party.jpg', upload_to='static/imgs/party/'),
        ),
    ]
