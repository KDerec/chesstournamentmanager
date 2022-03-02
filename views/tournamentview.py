"""Display tournament messages."""


from views import userinput


def change_the_number_of_rounds():
    """Display number of rounds modification and return user choice."""
    print("Le nombre de tour par défaut est de 4. Souhaitez-vous le modifier ?")

    return userinput.input_choice()


def add_a_description():
    """Display add a description and return user choice."""
    print("Ajouter une description ?")

    return userinput.input_choice()


def how_many_player_will_play():
    """Display how many player will player and return a number."""
    print("Combien de joueur vont participer au tournoi ? (inscrire un nombre pair): ")

    return userinput.input_a_number()


def wich_player_will_play():
    """Display select a player by number and return a number."""
    print("Sélectionner un joueur à ajouter au tournoi avec son numéro. ")

    return userinput.input_a_number()


def validate_chosen_players():
    """Display validate chosen player and return user choice."""
    print("Validez-vous cette sélection de joueur et démarrer le tournoi ?")

    return userinput.input_choice()


def validate_creation():
    """Display validation tournament creation and return user choice."""
    print("Validez-vous la création du tournoi ? Si non, retour menu tournoi.")

    return userinput.input_choice()


def display_start_tournament():
    """Display start tournament."""
    print("Le tournoi démarre !")


def return_in_tournament():
    """Display return in tournament message and return user choice."""
    print("Revenir au tournoi ?")

    return userinput.input_choice()


def display_standings(player_matchmaking, classement, i):
    """Display standings of the tournament."""
    print(
        f"{i+1}# avec {classement[player_matchmaking[i]]} points: "
        f"{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}"
    )


def tournament_is_not_over(tournament):
    print(
        f"Le tournoi '{tournament['name']}' n'est pas terminé "
        f"(il reste {tournament['number_of_rounds'] - len(tournament['rounds_list'])} tours à jouer). "
        "Continuer ce tournoi ?"
    )

    return userinput.input_choice()
