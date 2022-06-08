# Generated by Django 4.0.5 on 2022-06-03 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_remove_category_description_remove_movie_tagline'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTrailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('trailer', models.FileField(blank=True, null=True, upload_to='', verbose_name='Трейлер')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Трейлер',
                'verbose_name_plural': 'Трейлер',
            },
        ),
        migrations.DeleteModel(
            name='MovieShots',
        ),
    ]