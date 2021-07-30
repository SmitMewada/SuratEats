# Generated by Django 3.2.4 on 2021-06-12 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0022_order_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.address'),
        ),
    ]