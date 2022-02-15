"""Display reporting messages."""

from models.encoder import encode_json_to_str
from views import userinput


def display_players_report(player_list):
    for player in player_list:
        print(encode_json_to_str(player))  


def display_all_tournament_report(tournament_list):
    for tournament in tournament_list:
        print(encode_json_to_str(tournament))


class DisplayTournamentPlayersReport:

    def __init__():
        pass

    def by_alphabetical_order():
        pass

    def by_rank_order():
        pass


def display_all_rounds_tournament_report(tournament):
    pass


def display_all_matchs_tournament_report(tournament):
    pass


def choice_report_to_display():
    print('''Quel rapport souhaitez-vous afficher ?
            1. Liste de tous les acteurs,
            2. Liste de tous les joueurs d'un tournoi,
            3. Liste de tous les tournois,
            4. Liste de tous les tours d'un tournoi,
            5. Liste de tous les matchs d'un tournoi,
            6. Retour.''')

    return userinput.input_a_number()


def wich_order():
    print('''Par ordre :
            1. Alphabétique,
            2. Classement croissant,
            3. Retour.''')

    return userinput.input_a_number()


def select_tournament_number():
    print('Sélectionnez un numéro de tournoi : ')

    return userinput.input_a_number()