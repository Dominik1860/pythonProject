# Generated by Django 3.1.3 on 2020-11-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201110_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
