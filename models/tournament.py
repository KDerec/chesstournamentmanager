"""Define tournament object."""


class Tournament:

    mode = {0: 'bullet', 1: 'blitz', 2: 'rapide'}

    def __init__(self, name, location, date, time_controller, number_of_rounds,
                description):
        """Initiate tournament object."""

        self.name = name
        self.location = location
        self.date = date
        self.time_controller = time_controller
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.rounds_list = []
        self.players_list = []

    def add_player_in_players_list(self, player):
        """Add player object in tournament players list attribut."""

        self.players_list.append(player)
        player.display_added_player_message()

    def add_round_in_rounds_list(self, round):
        """Add round object in tournament rounds list attribut."""

        self.rounds_list.append(round)

    def display_player_in_tournament(self):
        """Display each player object in tournament players list attribut."""
        
        print('Les joueurs suivant participent au tournois :')
        for player in self.players_list:
            print(f'{self.players_list.index(player)}. {player.last_name} {player.first_name} ({player.rank})')

    def display_summary(self):
        """Display tournament attributs."""

        print(f'''Récapitulatif :
        Nom du tournoi: {self.name}
        Localisation: {self.location}
        Mode de jeux: {self.time_controller}
        Durée du tournoi: {self.duration} jours
        Nombre de tour: {self.number_of_rounds}
        Description: {self.description}''')
    