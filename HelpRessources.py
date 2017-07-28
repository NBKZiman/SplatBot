help_dict = {}

help_dict['version'] = "Affiche la version actuel du bot"

help_dict['help_ping'] = "Le bot répond pong"

help_dict['help_mangay'] = "!mangay [catégorie] [hasard]. Le bot affiche la liste des lieux où l'on peut manger selon "\
                           "la catégorie choisie, si il n'y a pas de catégorie le bot affiche toutes les possibilités."\
                           " On peut ajouter l'option hasard pour tirer le lieu au hasard. Les catégories sont :\n - " \
                           "fastfood\n - burger\n - commande \n - gluten-free\n - cher (qui n'est pas forcément cher " \
                           "mais il faut se déplacer pour y aller)"

help_dict['help_!help'] = "Les commandes disponibles sont : `!splat`,`!feriés`, `!seconde`," \
                          " `!help`, `!estCeQueJeDoisFaireG1'`, `!quiEstCe?`,`!perdu`" \
                          " `!version`, `!gitHub`, `!theGame`, `!starBurrito`, `!bite` et ses" \
                          " variantes `!stabo`, `!stabbo` et `!burrito`, `!mangay` et enfin `" \
                          "!log` . Tapez !help <commande> pour avoir plus d'infos sur une commande (sans le !)."

help_dict['help_splat'] = "!splat <jour> <mois> <année>.Sans arguments la fonction renvoie la date Splatonique du " \
                          "jour, on peut fournir une date en argument pour la convertir en date Splatonique, le bot" \
                          " vous insultera si la date n'est pas valide."

help_dict['help_bite'] = "!bite <nombre de ligne> <nombre d'aubergines>. Le bot affiche le nombre d'aubergine désiré,"\
                         " par défaut il y a une ligne de 20 aubergines. On peut afficher au maximum 10 lignes de" \
                         " 25 aubergines."

help_dict['help_burrito'] = "!burrito <nombre de ligne> <nombre de burrito>. Le bot affiche le nombre de burrito " \
                            "désiré, par défaut il y a une ligne de 20 burritos. On peut afficher au maximum 10" \
                            " lignes de 25 burritos. :burrito:"

help_dict['help_stabbo'] = "!stabbo <nombre de ligne> <nombre de couteau>. Le bot affiche le nombre de couteau " \
                            "désiré, par défaut il y a une ligne de 20 couteaux. On peut afficher au maximum 10" \
                            " lignes de 25 couteaux. :dagger:"

help_dict['help_stabo'] = "!stabo <nombre de ligne> <nombre de couteau>. Le bot affiche le nombre de couteau " \
                            "désiré, par défaut il y a une ligne de 20 couteaux. On peut afficher au maximum 10" \
                            " lignes de 25 couteaux. :knife:"

help_dict['help_cato'] = "!cato <nombre de ligne> <nombre de chat>. Le bot affiche le nombre de chat " \
                            "désiré, par défaut il y a une ligne de 20 chats. On peut afficher au maximum 10" \
                            " lignes de 25 couteaux. :cat:"

help_dict['help_doggo'] = "!cato <nombre de ligne> <nombre de chien>. Le bot affiche le nombre de chien " \
                            "désiré, par défaut il y a une ligne de 20 chiens. On peut afficher au maximum 10" \
                            " lignes de 25 couteaux. :cat:"

help_dict['help_férié'] = "!férié <jour> <mois> <année>. Par défaut, détermine si la date d'aujourd'hui est un jour" \
                          " férié selon le SplatCalendar. On peut lui passer une date en argument pour savoir si le" \
                          " jour dit est férié."

help_dict['help_help'] = "Vous êtes perdu ? vous ne savez plus quoi faire ? http://help.fr/"

help_dict['help_seconde'] = "Affiche le nombre de seconde qu'il s'est écoulé depuis le splat"

help_dict['help_estCeQueJeVaisFaireG1'] = "Répond oui, c'est pas comme si il y avait de l'espoir en même temps"

help_dict['help_quiEstCe?'] = "Le bot se présente"

help_dict['help_perdu'] = "Fais perdre le bot"

help_dict['help_gitHub'] = "Affiche le github du bot, vous pouvez venir aider à sa conception si vous le voulez"

help_dict['help_theGame'] = "!theGame [argument]. Trois perdus sont envoyés sur le chan à des moments aléatoires " \
                            "après l'émission de la commande. Vous pouvez mettre en argument un nombre de seconde" \
                            " maximum d'attente ou le nom de quelqu'un que vous voulez faire perdre. Vous pouvez" \
                            " aussi passez l'argument pour faire perdre trois personne au hasard. On peut cumuler " \
                            "les arguments"

help_dict['help_jeuSemaine'] = "Affiche le jeu de la semaine."

help_dict['help_log'] = "Changements depuis la dernière version \n - ajout de !cato et !dogo " \
                        "\n - Mise à jour de help"


def get_help(commande: str) -> str:
    return help_dict['help_' + commande]
