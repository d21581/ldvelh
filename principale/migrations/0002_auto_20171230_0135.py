# Generated by Django 2.0 on 2017-12-30 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='joueur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Valeur_case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='personnage',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bibliotheque',
            name='livre',
        ),
        migrations.RemoveField(
            model_name='case',
            name='souscase',
        ),
        migrations.RemoveField(
            model_name='case',
            name='valeur',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='paragraphe',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='personnage',
        ),
        migrations.RemoveField(
            model_name='personnage',
            name='para_lu',
        ),
        migrations.AddField(
            model_name='case',
            name='livre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case', to='principale.Livre'),
        ),
        migrations.AddField(
            model_name='livre',
            name='bibliotheque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livre', to='principale.Bibliotheque'),
        ),
        migrations.AddField(
            model_name='para_lu',
            name='personnage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='para_lu', to='principale.Personnage'),
        ),
        migrations.AddField(
            model_name='paragraphe',
            name='livre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paragraphe', to='principale.Livre'),
        ),
        migrations.AddField(
            model_name='personnage',
            name='livre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnage', to='principale.Livre'),
        ),
        migrations.DeleteModel(
            name='Souscase',
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
        migrations.AddField(
            model_name='valeur_case',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='valeur_case', to='principale.Case'),
        ),
        migrations.AddField(
            model_name='valeur_case',
            name='personnage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='valeur_case', to='principale.Personnage'),
        ),
        migrations.AddField(
            model_name='personnage',
            name='joueur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnage', to='principale.Joueur'),
        ),
    ]