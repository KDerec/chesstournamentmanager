"""Définit un tour."""


class Round:
    def __init__(self, name, beginning_date, ending_date):
        """Initialise un tour."""
        self.name =  name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.matchs_list = []

    def add_match_to_matchs_list(self, match):
        """Ajoute un match à la liste de matchs du tour."""
        pass