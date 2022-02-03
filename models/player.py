"""Définit un joueur."""


class Player:

    possible_sexe = {0: 'Homme', 1: 'Femme'}
    
    def __init__(self, last_name, first_name, birthday, sexe, rank):
        """Initialise un joueur."""
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank
    
    def update_player_rank(self, new_rank):
        """Met à jour le classement du joueur."""
        self.rank = new_rank
        print(f'Le classement de {self.last_name} {self.first_name} est mis à jour ({self.rank}).')

    def display_summary(self):
        print(f'''Récapitulatif :
        Nom: {self.last_name}
        Prénom: {self.first_name}
        Date de naissance: {self.birthday}
        Sexe: {self.sexe}
        Classement: {self.rank}''')

    def display_added_player_message(self):
        print(f'{self.last_name} {self.first_name} est ajouté.\n')

