# Generated by Django 3.2.6 on 2021-08-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0029_rating_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
