"""Définit un tour."""


class Round:
    def __init__(self, name, beginning_date, ending_date):
        """Initialise un tour."""
        self.name =  name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.match_list = []

    def display_round_name(self):
        print(self.name)