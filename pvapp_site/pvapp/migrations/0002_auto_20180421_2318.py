# Generated by Django 2.1.dev20180420150614 on 2018-04-21 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pvapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='athlete_name',
            new_name='name',
        ),
    ]
