# Generated by Django 4.1.3 on 2023-06-21 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_script_script'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='script',
        ),
    ]
