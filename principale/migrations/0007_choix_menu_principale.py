# Generated by Django 2.0 on 2017-12-31 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principale', '0006_auto_20171230_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choix_menu_principale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(max_length=30)),
                ('lien', models.CharField(max_length=20)),
                ('aide', models.CharField(max_length=100, null=True)),
                ('ordre', models.IntegerField()),
            ],
        ),
    ]
