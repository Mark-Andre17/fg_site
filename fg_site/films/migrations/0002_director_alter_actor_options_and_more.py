# Generated by Django 4.0.5 on 2022-06-03 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('image', models.ImageField(upload_to='directors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актер', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.RemoveField(
            model_name='actor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='film_genre', to='films.genre', verbose_name='жанры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='Прeмьера в мире'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='films.director', verbose_name='режиссер'),
        ),
    ]
