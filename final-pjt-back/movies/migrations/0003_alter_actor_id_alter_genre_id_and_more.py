# Generated by Django 4.1.3 on 2022-11-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_trailer_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date_opened',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
