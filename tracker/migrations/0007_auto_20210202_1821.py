# Generated by Django 3.1.6 on 2021-02-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20210202_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
