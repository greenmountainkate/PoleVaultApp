# Generated by Django 2.1.dev20180420150614 on 2018-05-02 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pvapp', '0005_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_graph', models.ImageField(upload_to='')),
                ('speed_graph', models.ImageField(upload_to='')),
                ('stride_graph', models.ImageField(upload_to='')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvapp.Athlete')),
            ],
        ),
        migrations.RenameField(
            model_name='session',
            old_name='date',
            new_name='time',
        ),
        migrations.AddField(
            model_name='jump',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvapp.Session'),
        ),
    ]
