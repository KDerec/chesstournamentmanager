"""Define InputPlayer object."""


import names
import random
from models.player import Player


class PlayerInput(Player):
    def __init__(self, last_name=False, first_name=False, birthday=False,
                sexe=False, rank=False):
        """Initiate PlyayerInput object."""

        super().__init__(last_name, first_name, birthday, sexe, rank)

    def input_last_name(self):
        """Input player last name."""

        self.last_name = str(input('Quelle est le nom du joueur ? : '))

    def input_first_name(self):
        """Input player first name."""

        self.first_name = str(input('Quelle est le prénom du joueur ? : '))

    def input_birthday_day(self):
        """Input player birthday day."""

        return int(input('Jour de naissance: '))

    def input_birthday_month(self):
        """Input player birthday month."""

        return int(input('Mois de naissance: '))

    def input_birthday_year(self):
        """Input player birthday year."""

        return int(input('Année de naissance: '))

    def input_sexe(self):
        """Input player sexe."""

        print(f'Voici les sexes possible : {self.possible_sexe}.')
        return int(input(f'Quelle sexe choisissez-vous ? '
                            '(Tapez un chiffre) : '))

    def input_rank(self):
        """Input player rank."""

        self.rank = int(input('Classement du joueur: '))


class PlayerInputAuto(Player):
    """Automaded completion of PlayerInput attributs."""

    def __init__(self, last_name=False, first_name=False, birthday=False,
                sexe=False, rank=False):
        super().__init__(last_name, first_name, birthday, sexe, rank)

    def input_last_name(self):
        self.last_name = names.get_last_name()

    def input_first_name(self):
        self.first_name = names.get_first_name()

    def input_birthday_day(self):
        return random.randint(0, 31)

    def input_birthday_month(self):
        return random.randint(1, 12)

    def input_birthday_year(self):
        return random.randint(1900, 2006)

    def input_sexe(self):
        return random.randint(0, 1)

    def input_rank(self):
        self.rank = random.randint(0, 999)