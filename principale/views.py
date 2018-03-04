from django.shortcuts import render
from django.http import HttpResponse
from .models import Case, Paragraphe, Para_lu, Personnage, Joueur, Livre, Bibliotheque, Valeur_case, Choix_menu_principale, Donnees_site
from django.shortcuts import get_object_or_404


# Create your views here.

info_debug = []

def lister_les_personnages():
	return Personnage.objects.all() 

def lister_les_livres():
	return Livre.objects.all()

def lister_les_joueurs():
	return Joueur.objects.all()

def toutes_les_cases():
	return Case.objects.all()

def creer_liste_para_dispo(nbr_paras):
	liste_paras = []
	for x in range(nbr_paras):
		liste_paras.append(x+1)
	return liste_paras

def les_valeurs(nom_perso, dern_livre_nom):
	'''
		Structure des données:
			
		donnees = [titre case,valeur case]
	'''

	global info_debug

	cases_a_afficher = Case.objects.filter(livres__titre__exact=str(dern_livre_nom))
	
	les_valeurs = Valeur_case.objects.filter(personnage__nom__exact=str(nom_perso))
	# Remettre les valeurs dans le bon ordre (selon l'ordre des cases à afficher)
	liste_complete_ordonne = []
	nbr_cases = len(cases_a_afficher)
	#info_debug = []
	#info_debug.append([dern_livre_nom, nbr_cases, str(nom_perso), 'rien'])
	for une_case in cases_a_afficher:
		trouve = 'non'
		nbr_valeurs_inspectes=0
		for une_val in les_valeurs:
			if trouve == 'non':
				nom_case_relate = str(une_case.titre) + ' ' + str(une_case.ordre) #nom d'objet Case selon l'objet Valeur_case
				if str(une_val.case) == str(nom_case_relate):
					liste_complete_ordonne.append([str(une_case.titre), str(une_val.valeur)])
					trouve = 'oui'
				nbr_valeurs_inspectes+=1
				if trouve == 'non':
					if nbr_valeurs_inspectes >= nbr_cases:
						# aucune valeur trouve pour ce titre de case
						liste_complete_ordonne.append([str(une_case.titre), 'devrait_vide'])

			#info_debug.append([nom_case_relate, str(une_val.case), str(trouve), str(nbr_valeurs_inspectes)])

	return liste_complete_ordonne 
				

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
    dern_pers_notes = dern_livre_obj.notes
    #cases_a_afficher = Case.objects.filter(livres__titre__exact=dern_livre_nom)
    les_vals = les_valeurs(dern_pers.val_str, dern_livre_nom)
    liste_paras = creer_liste_para_dispo(Livre.objects.get(titre__exact=dern_livre_nom).nbr_paras)

    liste_paras_lu = Para_lu.objects.filter(personnage__nom__exact=dern_livre_obj.nom).order_by('ordre')
    nbr_paras_lu = len(liste_paras_lu)
 
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'les_pers':les_pers,
				 'les_livres':les_livres,
				 'les_joueurs':les_joueurs,
				 'dern_pers':dern_pers,
				 'dern_joueur':dern_joueur,
				 #'cases_a_afficher':cases_a_afficher,
				 'debugs':info_debug,
				 'notes':dern_pers_notes,
				 'nom_dern_livre':dern_livre_nom,
				 'liste_paras':liste_paras,
				 'liste_paras_lu':liste_paras_lu,
				 'nbr_paras_lu':nbr_paras_lu,
				 'les_vals':les_vals},
    )


def changerJoueurOuPerso(request):
	if request.method == 'POST':
		joueur = request.POST['joueur']
		personnage = request.POST['personnage']
		
		Donnees_site.objects.filter(nom='dernier_personnage').update(val_str=personnage)
		Donnees_site.objects.filter(nom='dernier_joueur').update(val_str=joueur)

		return HttpResponse('')

def changer_valeurs(request):
	if request.method == 'POST':
		tout_info_raw = request.POST
		'''
		Trouver le nom des la clés soummises (e.g. CHANCE, ENDURANCE, etc), parce qu'elles ne
		sont pas fixes.
		'''
		les_keys_inconnus = []
		
		lesKeysConnus = ['csrfmiddlewaretoken', 'personnage']
		
		for une_key in tout_info_raw.keys():
			if une_key not in lesKeysConnus:
				les_keys_inconnus.append(une_key)

		nom_perso = str(request.POST['personnage'])
		for une_cle in les_keys_inconnus:
			la_valeur = request.POST[une_cle]
			nom_case = une_cle
			if la_valeur != '':
				Valeur_case.objects.filter(case__titre=nom_case, personnage__nom=nom_perso).update(valeur=int(la_valeur))
			
		
		return HttpResponse('')	


def sauv_notes(request):
	if request.method == 'POST':
		tout_info_raw = request.POST
		nom_perso = str(request.POST['personnage'])
		texte = str(request.POST['notes'])
		Personnage.objects.filter(nom=nom_perso).update(notes=texte)
			
		
		return HttpResponse('')	


def ajouter_para_lu(request):
	if request.method == 'POST':
		#tout_info_raw = request.POST
		num_para = request.POST['numero']
		ordre = request.POST['ordre']
		nom_personnage = request.POST['personnage']
		pers_obj = Personnage.objects.get(nom=nom_personnage)
		Para_lu(personnage=pers_obj, ordre=int(ordre)+2, numero=int(num_para)).save()
			
		
		return HttpResponse('')	
	













