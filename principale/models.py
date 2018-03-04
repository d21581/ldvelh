from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

'''
class Souscase(models.Model):
	titre = models.CharField(max_length=20)
	nbr_char_disp = models.IntegerField()
	valeur = models.CharField(max_length=600)
	
	def __str__(self):
		return self.titre
'''
class Case(models.Model):
	titre = models.CharField(max_length=40)
	nbr_char_disp = models.IntegerField()
	livres = models.ManyToManyField('Livre', related_name='case')
	ordre = models.IntegerField()

	class Meta:
		ordering = ["ordre", "titre"]

	def __str__(self):
		return '%s %d' % (self.titre, self.ordre)

class Paragraphe(models.Model):
	numero = models.IntegerField()
	texte = models.TextField()
	image = models.CharField(max_length=50)
	livre = models.ForeignKey('Livre', related_name='paragraphe', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return str(self.numero)

class Para_lu(models.Model):
	numero = models.IntegerField()
	ordre = models.IntegerField()
	personnage = models.ForeignKey('Personnage', related_name='para_lu', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return str(self.numero)

class Personnage(models.Model):
	nom = models.CharField(max_length=30, unique=True)
	notes = models.TextField(blank=True)
	joueur = models.ForeignKey('Joueur', related_name='personnage', on_delete=models.SET_NULL, null=True)
	livre = models.ForeignKey('Livre', related_name='personnage', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.nom

class Joueur(models.Model):
	nom = models.CharField(max_length=20, unique=True)
	user = models.ForeignKey(User, related_name='joueur', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.nom

class Livre(models.Model):
	titre = models.CharField(max_length=100, unique=True)
	bibliotheque = models.ForeignKey('Bibliotheque', related_name='livre', on_delete=models.SET_NULL, null=True)
	nbr_paras = models.IntegerField(default=400)

	def __str__(self):
		return self.titre

class Bibliotheque(models.Model):
	nom = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.nom

class Valeur_case(models.Model):
	case = models.ForeignKey(Case, related_name='valeur_case', on_delete=models.SET_NULL, null=True)
	valeur = models.CharField(max_length=30)
	personnage = models.ForeignKey(Personnage, related_name='valeur_case', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		#return self.case
		return "%s -- %s -- %s" % (self.personnage, self.case, self.valeur)

class Choix_menu_principale(models.Model):
	texte = models.CharField(max_length=30)
	lien = models.CharField(max_length=20)
	aide = models.CharField(max_length=100, null=True)
	ordre = models.IntegerField()

	def __str__(self):
		return self.texte

class Donnees_site(models.Model):
	nom = models.CharField(max_length=30)
	val_str = models.CharField(max_length=30, blank=True, null=True)
	val_int = models.IntegerField(blank=True, null=True)
	explication = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return self.nom
