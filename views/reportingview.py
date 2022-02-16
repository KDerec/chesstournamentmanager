"""Display reporting messages."""


from models.encoder import encode_json_to_str
from views import userinput


def display_players_report(player_list):
    """Display each player of players list."""
    for player in player_list:
        print(encode_json_to_str(player))


def display_all_tournament_report(tournament_list):
    """Display each tournament of tournaments list."""
    for tournament in tournament_list:
        print(encode_json_to_str(tournament))


def display_all_rounds_tournament_report(tournament_rounds_list):
    """Display each round of rounds list."""
    for round in tournament_rounds_list:
        print(encode_json_to_str(round))


def display_all_matchs_tournament_report(tournament_matchs_list):
    """Display each match of matchs list."""
    for match in tournament_matchs_list:
        print(encode_json_to_str(match))


def choice_report_to_display():
    """Display report menu and return number input."""
    print(
        """Quel rapport souhaitez-vous afficher ?
            1. Liste de tous les acteurs,
            2. Liste de tous les joueurs d'un tournoi,
            3. Liste de tous les tournois,
            4. Liste de tous les tours d'un tournoi,
            5. Liste de tous les matchs d'un tournoi,
            6. Retour."""
    )

    return userinput.input_a_number()


def wich_order():
    """Display order option and return number input."""
    print(
        """Par ordre :
            1. Alphabétique,
            2. Classement croissant,
            3. Retour."""
    )

    return userinput.input_a_number()


def select_tournament_number():
    """Display select tournament number and return number input."""
    print("Sélectionnez un numéro de tournoi : ")

    return userinput.input_a_number()
