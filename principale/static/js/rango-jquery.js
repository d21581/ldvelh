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
			de1=de1.toString();
			de2=de2.toString();
			resultat=total/*.concat('(', de2.toString());/*.concat('(').concat(de1).concat('+').concat(de2).concat(')')*/
			/*resultat = chiffreAleatoire(2, 12);*/
			resultat=de1 + '+' + de2 + '=' + total.toString();
			$('#resultat-2d6').text(resultat);
	    });

		/*$(document).on('submit', '#formulaire_choix_perso_joueur', function(e){*/
		jQuery('#changer-joueur-perso-btn').click(function(e){
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
			var sub_nat_d = 7;			
			var sub_nat_f = 8;			
			var sub_num_d = 5;			
			var sub_num_f = 6;
			if (id_bout_clique.length > 9){
				sub_num_f += 1;
				sub_nat_d += 1;
				sub_nat_f += 1;
			}	
			var nature_op = id_bout_clique.substring(sub_nat_d, sub_nat_f);
			var num_a_change = id_bout_clique.substring(sub_num_d, sub_num_f);
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
		
		
		$('.bout_ajust_combat').click(function(){
			var id_bout_clique = this.id;
			var sub_nat_d = 7;			
			var sub_nat_f = 8;			
			var sub_num_d = 5;			
			var sub_num_f = 6;
			if (id_bout_clique.length > 9){
				sub_num_f += 1;
				sub_nat_d += 1;
				sub_nat_f += 1;
			}	
			var nature_op = id_bout_clique.substring(sub_nat_d, sub_nat_f);
			var num_a_change = id_bout_clique.substring(sub_num_d, sub_num_f);
			var prefix = "val_";
			var id_val_a_change = prefix.concat(num_a_change);
			var valeur_a_change = parseInt($('#'+id_val_a_change).text());
			if (nature_op == '+') {
				var nouv_valeur = parseInt(valeur_a_change+1);	
			}
			if (nature_op == '-') {
				var nouv_valeur = parseInt(valeur_a_change-1);
			}
			$('#'+id_val_a_change).html(nouv_valeur);
		});


		$('#des_comb_btn').click(function(){
			var hab_pers = $('td:contains("HABILETÉ")').next('td').text();
			var hab_pers_mod =  $('[name="HABILETÉ"]').val();
			if (hab_pers_mod != '') {
				hab_pers = hab_pers_mod
			}
			var hab_en = $('#val_98').text();
			
			var de1_pers = chiffreAleatoire(1,6); 
			var de2_pers = chiffreAleatoire(1,6); 
			var de1_en = chiffreAleatoire(1,6); 
			var de2_en = chiffreAleatoire(1,6); 

			var tot_pers = parseInt(hab_pers) + parseInt(de1_pers) + parseInt(de2_pers);
			var tot_en = parseInt(hab_en) + parseInt(de1_en) + parseInt(de2_en);

			$('#resul_comb_pers').html(hab_pers.toString() + ' + ' + de1_pers.toString() + ' + ' + de2_pers.toString() + ' = ' + tot_pers.toString());
			$('#resul_comb_en').html(hab_en.toString() + ' + ' + de1_en.toString() + ' + ' + de2_en.toString() + ' = ' + tot_en.toString());
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
