# Generated by Django 3.1.6 on 2021-03-16 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('some', '0002_auto_20210315_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='free',
            new_name='busy',
        ),
    ]
