# Generated by Django 4.0.5 on 2022-06-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_actor_slug_genre_slug_producer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Жанр'),
        ),
    ]