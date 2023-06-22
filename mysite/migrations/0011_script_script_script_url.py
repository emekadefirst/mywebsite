# Generated by Django 4.1.3 on 2023-06-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_remove_script_script_alter_script_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='script',
            field=models.FileField(default=True, upload_to='scripts/'),
        ),
        migrations.AddField(
            model_name='script',
            name='url',
            field=models.CharField(default='your_default_value_here', max_length=255),
        ),
    ]
