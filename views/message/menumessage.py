"""Define the menus."""


from views.input import menuinput


def display_main_menu():
    """Display main menu and return a user choice."""
    print('''Menu principal :
        1. Tournoi ->
        2. Joueurs ->
        3. Rapports ->
        4. Quitter.
        ''')

    return menuinput.input_a_number()


def display_tournament_menu():
    """Display tournament menu and return a user choice."""
    print('''Menu tournoi :
        1. Commencer un tournoi ->
        2. Retour <-
        ''')
    
    return menuinput.input_a_number()


def display_player_menu():
    """Display player menu and return a user choice."""
    print('''Menu joueur :
        1. Ajouter un nouveau joueur à la base de donnée ->
        2. Supprimer un joueur de la base de donnée ->
        3. Retour <-
        ''')

    return menuinput.input_a_number()


def display_report_menu():
    """Display report menu and return a user choice."""
    print('''Menu rapport :
        1. Afficher un rapport ->
        2. Exporter un rapport ->
        3. Retour <-
        ''')
    
    return menuinput.input_a_number()


def display_exit_message():
      """Display exit message and return a user choice."""
      print('Tapez la lettre "q" pour confirmez l\'arrêt de l\'application : ')

      return input()


def display_how_many_player_will_play():
    print('Combien de joueur vont participer au tournoi ? : ')

    return menuinput.input_a_number()

def display_wich_player_will_play():
    print('Sélectionner un joueur à ajouter au tournoi avec son numéro. ')

    return menuinput.input_a_number()

def display_validate_chosen_players():
    print('Validez-vous cette sélection de joueur et démarrer le tournoi ?')

    return menuinput.input_choice()

def display_ready_to_start_tournament():
    print('Le tournoi démarre !')


def display_start_round(self):
    print(f'Commencer le tour {self+1} ?')

    return menuinput.input_choice()


def display_end_round(self):
    print(f'Terminer le tour {self+1} ?')

    return menuinput.input_choice()

def display_first_round_versus(i, top_players, low_players):
    print(f'Match #{i+1} : '
    f'{top_players[i].first_name} {top_players[i].last_name} vs '
    f'{low_players[i].first_name} {low_players[i].last_name}')


def display_other_round_versus(i, p1, d1):
    print(f'Match #{i+1} : '
        f'{p1[i].first_name} {p1[i].last_name} ({d1[p1[i]]}) vs '
        f'{p1[i+1].first_name} {p1[i+1].last_name} ({d1[p1[i+1]]})')

def display_players_already_played_together(player_one, player_two):
    print(f'{player_one.last_name} à déjà joué avec {player_two.last_name}.')


