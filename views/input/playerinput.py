import names
import random
from models.player import Player


class PlayerInput(Player):
    def __init__(self, last_name=False, first_name=False, birthday=False,
                sexe=False, rank=False):
        super().__init__(last_name, first_name, birthday, sexe, rank)

    def input_last_name(self):
        self.last_name = str(input('Quelle est le nom du joueur ? : ')) # names.get_last_name()

    def input_first_name(self):
        self.first_name = str(input('Quelle est le prénom du joueur ? : ')) # names.get_first_name()

    def input_birthday_day(self):
        return int(input('Jour de naissance: ')) # random.randint(0, 31)

    def input_birthday_month(self):
        return int(input('Mois de naissance: ')) # random.randint(1, 12)

    def input_birthday_year(self):
        return int(input('Année de naissance: ')) # random.randint(1900, 2006)

    def input_sexe(self):
        print(f'Voici les sexes possible : {self.possible_sexe}.')
        return int(input(f'Quelle sexe choisissez-vous ? '
                            '(Tapez un chiffre) : ')) # random.randint(0, 1)

    def input_rank(self):
        self.rank = int(input('Classement du joueur: ')) # random.randint(0, 999)

    def input_choice(self):
        return input('Oui = o : ')

    def validate_creation(self):
        print('Validez-vous la création du joueur ? '
                'Si non, retour menu joueur.')
        choice = self.input_choice() # 'O'
        if choice.upper() == 'O':
            return True
        else:
            return False


class PlayerInputAuto(Player):
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

    def input_choice(self):
        return input('Oui = o : ')

    def validate_creation(self):
        choice = 'O'
        if choice.upper() == 'O':
            return True
        else:
            return False