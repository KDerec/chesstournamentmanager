"""Définit un tournoi."""


class Tournament:

    mode = {0: 'bullet', 1: 'blitz', 2: 'rapide'}

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
        self.players_list.append(player)
        player.display_added_player_message()

    def add_round_in_rounds_list(self, round):
        """Ajoute un tour au tournoi."""
        self.rounds_list.append(round)

    def display_player_in_tournament(self):
        print('Les joueurs suivant participent au tournois :')
        for player in self.players_list:
            print(f'{self.players_list.index(player)}. {player.last_name} {player.first_name} ({player.rank})')