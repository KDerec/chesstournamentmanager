"""Définit un joueur."""

import names
import random


class Player:
    def __init__(self, last_name, first_name, birthday, sexe, rank):
        """Initialise un joueur."""
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank
    
    def update_player_rank(self, rank):
        """Met à jour le classement du joueur."""
        self.rank = rank


def create_player():
    ''''Préparation des attributs d'un joueur'''
    last_name = names.get_last_name() #input('Nom du joueur: ')
    first_name = names.get_first_name() #input('Prénom du joueur: ')
    day_birthday = str(random.randint(0, 31)) #str(input('Jour de naissance: '))
    month_birthday = str(random.randint(1, 12)) #str(input('Mois de naissance: '))
    year_birthday = str(random.randint(1900, 2006)) #str(input('Année de naissance: '))
    birthday = year_birthday + '-' + month_birthday + '-' + day_birthday
    sexe = {1: 'Homme', 2: 'Femme'}
    #print(f'{sexe}.')
    choice = random.randint(1, 2) #int(input('Quel sexe ? (1 ou 2)'))
    sexe = sexe[choice]
    rank = random.randint(0, 999) #int(input('Classement du joueur: '))
    if rank < 0:
        while rank < 0:
            print('Le classement ne peux pas être négatif.')
            rank = int(input('Classement du joueur: '))
    # print(f'''Récapitulatif :
    # Nom: {last_name}
    # Prénom: {first_name}
    # Date de naissance: {birthday}
    # Sexe: {sexe}
    # Classement: {rank}''')
    choice = 'O' #input('Validez-vous la création du joueur ? Oui = o')
    if choice.upper() == 'O':
        player = Player(last_name, first_name, birthday, sexe, rank)
    
        return player

def select_random_player_in_database(self):
    '''Simule le choix de 8 joueurs dans la base de données.'''
    return random.sample(self, 8)