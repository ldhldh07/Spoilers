# Generated by Django 4.1.3 on 2022-11-18 01:21


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_trailer_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
