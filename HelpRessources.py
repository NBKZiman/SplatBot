help_dict = {}

help_dict['version'] = "Affiche la version actuel du bot"

help_dict['help_ping'] = "Le bot répond pong"

help_dict['help_mangay'] = "!mangay [catégorie] [hasard]. Le bot affiche la liste des lieux où l'on peut manger selon "\
                           "la catégorie choisie, si il n'y a pas de catégorie le bot affiche toutes les possibilités."\
                           " On peut ajouter l'option hasard pour tirer le lieu au hasard. Les catégories sont :\n - " \
                           "fastfood\n - burger\n - commande \n - gluten-free\n - cher (qui n'est pas forcément cher " \
                           "mais il faut se déplacer pour y aller)"

help_dict['help_!help'] = "Les commandes disponibles sont : !splat, !feriés, !seconde, !help, !estCeQueJeDoisFaireG1'" \
                         ", !quiEstCe?,! perdu !version, !gitHub et !theGame. Tapez !help <commande> pour avoir plus" \
                         " d'infos sur une commande (sans le !)."

help_dict['help_splat'] = "!splat <jour> <mois> <année>.Sans arguments la fonction renvoie la date Splatonique du " \
                          "jour, on peut fournir une date en argument pour la convertir en date Splatonique, le bot" \
                          " vous insultera si la date n'est pas valide."

help_dict['help_bite'] = "!bite <nombre de ligne> <nombre d'aubergines>. Le bot affiche le nombre d'aubergine désiré,"\
                         " par défaut il y a une ligne de 20 aubergines. On peut afficher au maximum 10 lignes de" \
                         " 25 aubergines."

help_dict['help_férié'] = "!férié <jour> <mois> <année>. Par défaut, détermine si la date d'aujourd'hui est un jour" \
                          " férié selon le SplatCalendar. On peut lui passer une date en argument pour savoir si le" \
                          " jour dit est férié."

help_dict['help_help'] = "Vous êtes perdu ? vous ne savez plus quoi faire ? http://help.fr/"

help_dict['help_seconde'] = "Affiche le nombre de seconde qu'il s'est écoulé depuis le splat"

help_dict['help_estCeQueJeVaisFaireG1'] = "Répond oui, c'est pas comme si il y avait de l'espoir en même temps"

help_dict['help_quiEstCe?'] = "Le bot se présente"

help_dict['help_perdu'] = "Fais perdre le bot"

help_dict['help_gitHub'] = "Affiche le github du bot, vous pouvez venir aider à sa conception si vous le voulez"

help_dict['help_theGame'] = "Trois perdus sont envoyés sur le chan à des moments aléatoires après l'émission de la " \
                            "commande. Vous pouvez mettre en argument un nombre de seconde maximum d'attente ou le " \
                            "nom de quelqu'un que vous voulez faire perdre."
help_dict['help_log'] = "Changement depuis la dernière version \n - Création de la commande log \n - Mise à jour de " \
                        "la commande !estCeQueJeVaisFaireG1 \n - Ajout du ping aléatoire lors de la commande !theGame" \
                        "et du timer modifiable"


def get_help(commande: str) -> str:
    return help_dict['help_' + commande]




