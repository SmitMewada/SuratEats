# Generated by Django 3.2.4 on 2021-06-04 13:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_category_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='house',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='street',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.customer')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('order_date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.customer')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.dish')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.restaurant')),
            ],
        ),
    ]
