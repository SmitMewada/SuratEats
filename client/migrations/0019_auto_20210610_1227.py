# Generated by Django 3.2.4 on 2021-06-10 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_auto_20210610_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='transaction',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.order'),
        ),
    ]
