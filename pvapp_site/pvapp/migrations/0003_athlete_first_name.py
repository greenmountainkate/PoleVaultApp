# Generated by Django 2.1.dev20180420150614 on 2018-04-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvapp', '0002_auto_20180421_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
