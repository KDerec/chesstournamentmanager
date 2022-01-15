"""Définit un tournoi."""

import datetime
from datetime import timedelta


class Tournament:
    def __init__(self, name, location, date, time_controller, number_of_rounds,
                description):
        """Initialise un tournoi."""
        self.name = name
        self.location = location
        self.date = date
        self.time_controller = time_controller
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.rounds_list = []
        self.players_list = []

    def add_player_in_players_list(self, player):
        """Ajoute un joueur dans le tournoi."""
        pass

    def remove_player_from_players_list(self, player):
        """Retire un joueur dans le tournoi."""
        pass

    def add_round_in_rounds_list(self, round):
        """Ajoute un tour au tournoi."""
        pass

    def update_player_ranking(self, player):
        """Met à jour le classement d'un joueur du tournoi."""
        pass


def create_tournament():
    """Préparation des attributs du tournoi."""
    name = 'The tournoi' #input('Quelle est le nom du tournoi ? : ')
    location = 'Paris' #input('Où ce déroule le tournoi ? : ')
    mode = {1: 'bullet', 2: 'blitz', 3: 'rapide'}
    print(f'Voici les modes de gestion de temps {mode}.')
    choice = 1 #int(input('Quelle mode de choisissez_vous ? (1, 2 ou 3)'))
    time_controller = mode[choice]
    duration = 2 #int(input('Combien de jour le tournoi vas-t-il durer ? : '))
    choice = '' #input(
    #'Le nombre de tour est de 4, souhaitez-vous le modifier ? Oui = o: ')
    if choice.upper() == 'O':
        number_of_rounds = int(input('Combien de tour ? : '))
    else:
        number_of_rounds = 4

    choice = '' #input('Ajouter une description ? Oui = o')
    if choice.upper() == 'O':
        description = input('Votre description : ')
    else:
        description = ''
    print(f'''Récapitulatif :
    Nom du tournoi: {name}
    Localisation: {location}
    Mode de jeux: {time_controller}
    Durée du tournoi: {duration} jours
    Nombre de tour: {number_of_rounds}
    Description: {description}''')
    choice = 'O' #input('Validez-vous la création du tournoi ? Oui = o')
    if choice.upper() == 'O':
        if duration > 1:
            first_day = datetime.date.today()
            last_day = first_day + timedelta(days=duration-1)
            date = str(first_day) + '_' + str(last_day)
        else:
            date = str(datetime.date.today())
        tournament = Tournament(name, location, date, time_controller,
                                number_of_rounds, description)
        return tournament