# Generated by Django 3.2.4 on 2021-06-12 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_remove_transaction_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='order',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.order'),
        ),
        migrations.AlterField(
            model_name='address',
            name='restaurant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.restaurant'),
        ),
    ]
