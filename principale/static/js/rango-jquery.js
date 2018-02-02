$(document).ready(function() {

        // JQuery code to be added in here.

		function chiffreAleatoire(min,max)
		{
    		return Math.floor(Math.random()*(max-min+1)+min);
		}


		$("#lancer_de").click( function(event) {
			resultat = chiffreAleatoire(1, 6);
			$('#resultat').text(resultat);
	    });
		
		$("#lancer_2des").click( function(event) {
			de1=chiffreAleatoire(1, 6);
			de2=chiffreAleatoire(1, 6);
			total=de1+de2;
			resultat=total/*.concat('(', de2.toString());/*.concat('(').concat(de1).concat('+').concat(de2).concat(')')*/
			/*resultat = chiffreAleatoire(2, 12);*/
			$('#resultat-2d6').text(resultat);
	    });

		/*$(document).on('submit', '#formulaire_choix_perso_joueur', function(e){*/
		jQuery('#formulaire_choix_perso_joueur').click(function(e){
			e.preventDefault();
			/*$.ajax({*/
			jQuery.ajax({
				type:'POST',
				url:'/principale/changer_joueur_ou_perso/',
				data:{
					joueur:$('#selection_joueur').val(),
					personnage:$('#selection_personnage').val(),
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
				},
				success:function(response){
					console.log(response);
					location.reload();
				}
			})

		});

		$('.bout_ajust').click(function(){
			var id_bout_clique = this.id;
			var nature_op = id_bout_clique.substring(7, 8);
			var num_a_change = id_bout_clique.substring(5, 6);
			var prefix = "val_";
			var prefix_org = "val_actuelle_";
			var id_val_a_change = prefix.concat(num_a_change);
			var id_val_org_a_change = prefix_org.concat(num_a_change);
			var valeur_a_change = parseInt($('#'+id_val_a_change).val());
			if (isNaN(valeur_a_change)) {
				valeur_a_change = parseInt($('#'+id_val_org_a_change).text());
			}
			if (nature_op == '+') {
				var nouv_valeur = valeur_a_change+1;	
			}
			if (nature_op == '-') {
				var nouv_valeur = valeur_a_change-1;
			}
			$('#'+id_val_a_change).val(nouv_valeur);
		});


		jQuery('#commettre-btn').click(function(e){
			e.preventDefault();
			var donnees = $("#tableau_valeurs").serialize();
			var nom_perso = $('#selection_personnage').val();
			var donnees_tout = donnees + "&personnage=" + nom_perso;
			jQuery.ajax({
				type:'POST',
				url:'/principale/changer_valeurs/',
				data:donnees_tout,
				success:function(response){
					location.reload();
				},
				error:function(response){
					alert('toujours pas...');
					console.log(response);
				}
			});
		});

		jQuery('#commettre-notes').click(function(e){
			e.preventDefault();
			var donnees = $("#form-notes").serialize();
			var nom_perso = $('#selection_personnage').val();
			var donnees_tout = donnees + "&personnage=" + nom_perso;
			/*$("#debugging").text(donnees_tout);*/
			jQuery.ajax({
				type:'POST',
				url:'/principale/sauv_notes/',
				data:donnees_tout,
				success:function(response){
					location.reload();
				},
				error:function(response){
					alert('toujours pas...');
					console.log(response);
				}
			});
		});
});
