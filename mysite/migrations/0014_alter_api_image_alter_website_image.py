# Generated by Django 4.1.3 on 2023-06-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_remove_script_script'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
