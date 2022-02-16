"""Define TournamentInput object."""


from models.tournament import Tournament


class InputTournament(Tournament):
    def __init__(
        self,
        name=False,
        location=False,
        date=False,
        time_controller=False,
        number_of_rounds=False,
        description=False,
        duration=False,
    ):
        """Initiate InputTournament object."""
        super().__init__(name, location, date, time_controller, number_of_rounds, description)
        self.duration = duration

    def input_name(self):
        """Input tournament name."""
        self.name = str(input("Quelle est le nom du tournoi ? : "))

    def input_location(self):
        """Input tournament location."""
        self.location = str(input("Où ce déroule le tournoi ? : "))

    def input_mode(self):
        """Display time controller mode and return user choice."""
        print(f"Voici les modes de gestion de temps : {self.mode}.")
        return int(input("Quelle mode choisissez-vous ? (Tapez un chiffre) : "))

    def input_duration(self):
        """Input tournament duration."""
        self.duration = int(input("Combien de jour le tournoi " "vas-t-il durer ? : "))

    def input_number_of_rounds(self):
        """Input number of rounds."""
        self.number_of_rounds = int(input("Combien de tour ? : "))

    def input_description(self):
        """Input description."""
        self.description = input("Votre description : ")
