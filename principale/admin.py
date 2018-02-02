from django.contrib import admin

# Register your models here.

from .models import Bibliotheque, Livre, Personnage, Paragraphe, Para_lu, Case, Joueur, Choix_menu_principale, Valeur_case, Donnees_site

admin.site.register(Bibliotheque)
admin.site.register(Livre)
admin.site.register(Personnage)
admin.site.register(Paragraphe)
admin.site.register(Para_lu)
admin.site.register(Case)
admin.site.register(Joueur)
admin.site.register(Choix_menu_principale)
admin.site.register(Valeur_case)
admin.site.register(Donnees_site)
