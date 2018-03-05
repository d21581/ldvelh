$(document).ready(function() {

        // JQuery code to be added in here.

		function chiffreAleatoire(min,max)
		{
    		return Math.floor(Math.random()*(max-min+1)+min);
		}


		function trouver_val_dune_case(nom_case){
			/* Trouver la valeur originale  */
			var val_orig = $("td").filter(function() {
    			return $(this).text() === nom_case;
			}).next('td').text();
			var val = val_orig;
			/* Trouver la valeur modifié  */
			var val_mod =  $('[name=' + nom_case + ']').val();
			if (val_mod != '') {
				val = val_mod;
			}
			return val;
		}

		$("#lancer_de").click( function(event) {
			resultat = chiffreAleatoire(1, 6);
			$('#resultat').text(resultat);
	    });
		
		$("#enlever_dernier_para_lu").click( function(event) {
			var ordre = $('.case_paras_lu:last').attr("id");
			var ordre_arr = ordre.split("_");
			var ordre_final = ordre_arr[(ordre_arr.length)-1];

			jQuery.ajax({
				type:'POST',
				url:'/principale/enlever_para_lu/',
				data:{
					personnage:$('#selection_personnage').val(),
					numero:$('.case_paras_lu').last().text(),
					ordre_para:  ordre_final,
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
				},
				success:function(response){
					console.log(response);
					location.reload();
				}
			})
		});
		
		$("#lancer_2des").click( function(event) {
			de1=chiffreAleatoire(1, 6);
			de2=chiffreAleatoire(1, 6);
			total=de1+de2;
			de1=de1.toString();
			de2=de2.toString();
			resultat=total
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


		$('.case_paras').click(function(){
			var para_clique = this.id;
			var long_string_id = para_clique.length;
			para_clique = para_clique.substring(5, long_string_id);
			var ordre = $('.case_paras_lu:first').attr("id");
			var ordre_arr = ordre.split("_");
			var ordre_final = ordre_arr[(ordre_arr.length)-1];
			var numero_formate = para_clique;
			var personnage_sel = $('#selection_personnage').val();

			jQuery.ajax({
				type:'POST',
				url:'/principale/ajouter_para_lu/',
				data:{
					ordre:ordre_final,
					numero:numero_formate,
					personnage:personnage_sel,
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
				},
				success:function(response){
					location.reload();
				},
				error:function(response){
					alert('toujours pas...');
					console.log(response);
				}
			});
			
		});

		$('#des_comb_btn').click(function(){

			hab_pers = trouver_val_dune_case("HABILETÉ");

			var hab_en = $('#val_98').text();
			
			var de1_pers = chiffreAleatoire(1,6); 
			var de2_pers = chiffreAleatoire(1,6); 
			var de1_en = chiffreAleatoire(1,6); 
			var de2_en = chiffreAleatoire(1,6); 

			var tot_pers = parseInt(hab_pers) + parseInt(de1_pers) + parseInt(de2_pers);
			var tot_en = parseInt(hab_en) + parseInt(de1_en) + parseInt(de2_en);

			$('#resul_comb_pers').html(hab_pers.toString() + ' + ' + de1_pers.toString() + ' + ' + de2_pers.toString() + ' = ' + tot_pers.toString());
			$('#resul_comb_en').html(hab_en.toString() + ' + ' + de1_en.toString() + ' + ' + de2_en.toString() + ' = ' + tot_en.toString());

			/* Enlever deux points d'endurance au perdant  */
			if (tot_pers > tot_en) { /* le joueur gagne  */
				end_act = parseInt($('#val_99').text());
				var nouv_val = end_act -2;
				$('#val_99').html(nouv_val);			
			}
			if (tot_en > tot_pers) { /* l'ennemie gagne  */
				end_act = trouver_val_dune_case("ENDURANCE");
				$("[name='ENDURANCE']").val(parseInt(end_act) - 2);
			}
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
