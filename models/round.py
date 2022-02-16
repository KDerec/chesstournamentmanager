"""Define round object."""


class Round:
    def __init__(self, name, beginning_date, ending_date):
        """Initate round object."""
        self.name = name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.match_list = []

    def display_round_name(self):
        """Display round name attribut."""
        print(self.name)
