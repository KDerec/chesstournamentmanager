from views import userinput


def change_the_number_of_rounds():
    print('Le nombre de tour par défaut est de 4. Souhaitez-vous le modifier ?')

    return userinput.input_choice()


def add_a_description():
    print('Ajouter une description ?')

    return userinput.input_choice()


def how_many_player_will_play():
    print('Combien de joueur vont participer au tournoi ? (inscrire un nombre pair): ')

    return userinput.input_a_number()


def wich_player_will_play():
    print('Sélectionner un joueur à ajouter au tournoi avec son numéro. ')

    return userinput.input_a_number()


def validate_chosen_players():
    print('Validez-vous cette sélection de joueur et démarrer le tournoi ?')

    return userinput.input_choice()


def validate_creation():
    print('Validez-vous la création du tournoi ? Si non, retour menu tournoi.')
    
    return userinput.input_choice()


def display_start_tournament():
    print('Le tournoi démarre !')


def display_standings(player_matchmaking, classement, i):
    print(f'{i+1}# avec {classement[player_matchmaking[i]]} points: '
        f'{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}')