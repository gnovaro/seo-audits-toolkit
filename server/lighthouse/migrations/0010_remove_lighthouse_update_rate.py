# Generated by Django 3.1.4 on 2020-12-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouse', '0009_auto_20201215_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lighthouse',
            name='update_rate',
        ),
    ]
