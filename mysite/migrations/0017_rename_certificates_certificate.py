# Generated by Django 4.1.3 on 2023-06-22 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_api_url_website_url_alter_script_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificates',
            new_name='Certificate',
        ),
    ]
