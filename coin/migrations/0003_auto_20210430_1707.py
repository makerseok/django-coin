# Generated by Django 3.2 on 2021-04-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_coindata_coin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coindata',
            name='acc_trade_volume_24h',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coindata',
            name='signed_change_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coindata',
            name='signed_change_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
