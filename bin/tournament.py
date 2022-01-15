"""Définit un tournoi."""


class Tournament:
    def __init__(self, name, location, date, time_controller, description,
                number_of_rounds=4):
        """Initialise un tournoi."""
        self.name = name
        self.location = location
        self.date = date
        self.time_controller = time_controller
        self.description = description
        self.number_of_rounds = number_of_rounds
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