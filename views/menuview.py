"""Define the menus."""


from views import userinput


def display_main_menu():
    """Display main menu and return a user choice."""
    print('''Menu principal :
        1. Tournoi ->
        2. Joueurs ->
        3. Rapports ->
        4. Quitter.
        ''')

    return userinput.input_a_number()


def display_tournament_menu():
    """Display tournament menu and return a user choice."""
    print('''Menu tournoi :
        1. Commencer un tournoi ->
        2. Retour <-
        ''')
    
    return userinput.input_a_number()


def display_player_menu():
    """Display player menu and return a user choice."""
    print('''Menu joueur :
        1. Ajouter un nouveau joueur à la base de donnée ->
        2. Retour <-
        ''')

    return userinput.input_a_number()


def display_report_menu():
    """Display report menu and return a user choice."""
    print('''Menu rapport :
        1. Afficher un rapport ->
        2. Exporter un rapport ->
        3. Retour <-
        ''')
    
    return userinput.input_a_number()

