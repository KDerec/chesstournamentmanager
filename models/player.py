"""Define player object."""


class Player:

    possible_sexe = {0: 'Homme', 1: 'Femme'}
    
    def __init__(self, last_name, first_name, birthday, sexe, rank):
        """Initiate player object."""

        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank
    
    def update_player_rank(self, new_rank):
        """Update player rank attribut."""

        self.rank = new_rank
        print(f'Le classement de {self.last_name} {self.first_name} est mis à jour ({self.rank}).')

    def display_summary(self):
        """Display player attributs."""

        print(f'''Récapitulatif :
        Nom: {self.last_name}
        Prénom: {self.first_name}
        Date de naissance: {self.birthday}
        Sexe: {self.sexe}
        Classement: {self.rank}''')

    def display_added_player_message(self):
        """Display added player message."""
        
        print(f'{self.last_name} {self.first_name} est ajouté.\n')

