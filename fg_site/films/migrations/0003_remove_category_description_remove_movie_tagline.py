# Generated by Django 4.0.5 on 2022-06-03 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_director_alter_actor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tagline',
        ),
    ]