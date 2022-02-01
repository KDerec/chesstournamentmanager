"""Define the menus."""


def display_main_menu():
    """Display main menu and return a user choice."""
    print('''Menu principal :
          1. Tournoi ->
          2. Joueurs ->
          3. Rapports ->
          4. Quitter.
          ''')
    
    choice = int(input('Sélectionnez un numéro (1, 2 ou 3) : '))

    return choice


def display_tournament_menu():
    """Display tournament menu and return a user choice."""
    print('''Menu tournoi :
          1. Commencer un tournoi ->
          2. Retour <-
          ''')
    
    choice = int(input('Sélectionnez un numéro (1 ou 2) : '))

    return choice


def display_player_menu():
    """Display player menu and return a user choice."""
    print('''Menu joueur :
          1. Ajouter un nouveau joueur à la base de donnée ->
          2. Supprimer un joueur de la base de donnée ->
          3. Retour <-
          ''')
    
    choice = int(input('Sélectionnez un numéro (1, 2 ou 3) : '))

    return choice


def display_report_menu():
    """Display report menu and return a user choice."""
    print('''Menu rapport :
          1. Afficher un rapport ->
          2. Exporter un rapport ->
          3. Retour <-
          ''')
    
    choice = int(input('Sélectionnez un numéro (1, 2 ou 3) : '))

    return choice

def display_exit_message():
      """Display exit message and return a user choice."""
      print('Tapez la lettre "q" pour confirmez l\'arrêt de l\'application : ')

      choice = input()

      return choice
