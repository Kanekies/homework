# Generated by Django 3.1.7 on 2021-03-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('some', '0004_auto_20210324_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]