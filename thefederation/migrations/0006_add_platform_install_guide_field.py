# Generated by Django 2.0.3 on 2018-04-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thefederation', '0005_add_more_fields_to_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='install_guide',
            field=models.URLField(blank=True, max_length=256),
        ),
    ]
