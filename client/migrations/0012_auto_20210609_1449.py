# Generated by Django 3.2.4 on 2021-06-09 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='client.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='restaurant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='client.restaurant'),
            preserve_default=False,
        ),
    ]
