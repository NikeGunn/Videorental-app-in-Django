# Generated by Django 4.0 on 2022-12-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_daily_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]
