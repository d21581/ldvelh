from django.shortcuts import render
from django.http import HttpResponse
from .models import Case, Paragraphe, Para_lu, Personnage, Joueur, Livre, Bibliotheque, Valeur_case, Choix_menu_principale, Donnees_site

# Create your views here.

def lister_les_personnages():
	return Personnage.objects.all() 

def lister_les_livres():
	return Livre.objects.all()

def lister_les_joueurs():
	return Joueur.objects.all()

def toutes_les_cases():
	return Case.objects.all()

def les_valeurs(nom_perso, liste_cases):
	les_valeurs = Valeur_case.objects.filter(personnage__nom__exact=nom_perso)
	liste_complete = []
	nbr_cases = len(liste_cases)
	for une_case in liste_cases:
		trouve = 'non'
		for une_val in les_valeurs:
			if trouve == 'non':
				if une_val.nom == une_case:
					liste_complete.append('autre test')#une_val.valeur)
					trouve = 'oui'
				x+=1
				if x == nbr_cases:
					liste_complete.append('test')
	dummy1 = ['a','b','c']
	dummy2 = [1,2,3]
	liste_complete = [dummy1, dummy2]
	return liste_complete
				

def index(request):
    """
    View function for home page of site.
    """

    les_livres = lister_les_livres
    les_joueurs = lister_les_joueurs
    les_pers = lister_les_personnages
    les_cases = toutes_les_cases

    dern_joueur = Donnees_site.objects.get(nom__exact='dernier_joueur')
    dern_pers = Donnees_site.objects.get(nom__exact='dernier_personnage')
    dern_livre_obj = Personnage.objects.get(nom__exact=dern_pers.val_str)
    dern_livre_nom = dern_livre_obj.livre
    cases_a_afficher = Case.objects.filter(livres__titre__exact=dern_livre_nom)
    nbr_cases = cases_a_afficher.count()
    les_vals = les_valeurs(dern_pers.val_str, cases_a_afficher)
    
 
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'les_pers':les_pers,
				 'les_livres':les_livres,
				 'les_joueurs':les_joueurs,
				 'dern_pers':dern_pers,
				 'dern_joueur':dern_joueur,
				 'cases_a_afficher':cases_a_afficher,
				 'nbr_cases':nbr_cases,
				 'les_vals':les_vals},
    )

