# Generated by Django 2.0 on 2018-01-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principale', '0012_donnees_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnees_site',
            name='explication',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='donnees_site',
            name='val_int',
            field=models.IntegerField(null=True),
        ),
    ]
