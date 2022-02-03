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
        2. Retour <-
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


def display_change_player_rank():
    print('Voulez-vous modifier le classement d\'un joueur ?')

    return menuinput.input_choice()

def display_select_a_player_to_change_his_rank():
    print('Sélectionner un joueur pour modifier son classement.')

    return menuinput.input_a_number()


def display_choice_new_rank():
    print('Entrer un nombre pour le nouveau classement : ')

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
    f'{top_players[i].first_name} {top_players[i].last_name} {top_players[i].rank} vs '
    f'{low_players[i].first_name} {low_players[i].last_name} {low_players[i].rank} (joue en blanc).')


def display_other_round_versus(i, p1, d1):
    print(f'Match #{i+1} : '
        f'{p1[i].first_name} {p1[i].last_name} ({d1[p1[i]]}) vs '
        f'{p1[i+1].first_name} {p1[i+1].last_name} ({d1[p1[i+1]]}) (joue en blanc).')

def display_players_already_played_together(player_one, player_two):
    print(f'{player_one.last_name} à déjà joué avec {player_two.last_name}.')


def display_standings(player_matchmaking, classement, i):
    print(f'{i+1}# avec {classement[player_matchmaking[i]]} points: '
        f'{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}')


def display_match_notation(i, players):
    print(f'\nNotation match #{i} : '
            f'{players[0].first_name} {players[0].last_name} vs '
            f'{players[1].first_name} {players[1].last_name}')


def display_note_the_match(players):
    print(f'Résulat de {players[0].first_name} {players[0].last_name} '
            '(1 pour gagner, 0 perdu, 0.5 pour égalité) : ')

    return menuinput.input_a_float()