# Generated by Django 2.2 on 2019-06-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0003_auto_20190615_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='num',
            field=models.IntegerField(default=1, verbose_name='购买票数'),
            preserve_default=False,
        ),
    ]
