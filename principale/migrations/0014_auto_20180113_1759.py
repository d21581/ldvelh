# Generated by Django 2.0 on 2018-01-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principale', '0013_auto_20180106_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donnees_site',
            name='explication',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donnees_site',
            name='val_int',
            field=models.IntegerField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donnees_site',
            name='val_str',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
    ]