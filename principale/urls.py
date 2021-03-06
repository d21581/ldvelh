from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^changer_joueur_ou_perso/$', views.changerJoueurOuPerso),
	url(r'^changer_valeurs/$', views.changer_valeurs),
	url(r'^sauv_notes/$', views.sauv_notes),
	url(r'^ajouter_para_lu/$', views.ajouter_para_lu),
	url(r'^enlever_para_lu/$', views.enlever_para_lu),
]
