# Generated by Django 3.2.4 on 2021-06-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20210604_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=150)),
                ('pincode', models.BigIntegerField()),
                ('area', models.CharField(max_length=150)),
            ],
        ),
    ]
