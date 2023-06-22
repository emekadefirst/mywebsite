# Generated by Django 4.1.3 on 2023-06-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_alter_api_id_alter_certificates_id_alter_message_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='url',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='url',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='script',
            name='url',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
