# Generated by Django 2.0 on 2017-12-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principale', '0002_auto_20171230_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='livre',
        ),
        migrations.AddField(
            model_name='case',
            name='livres',
            field=models.ManyToManyField(related_name='case', to='principale.Livre'),
        ),
    ]
