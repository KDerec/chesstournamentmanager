""""Définit un match."""

import random


def create_match_results(self):
    """Créer une liste de score."""
    i = 1
    results = []
    players = self
    while players != []:
        # print(f'\nNotation match #{i} : '
        # f'{players[0].first_name} {players[0].last_name} vs '
        # f'{players[1].first_name} {players[1].last_name}')
        while True:
            try:
                result_one = random.choice([0,0.5,1]) #float(input(f'Résulat de {players[0].first_name} ' 
                #f'{players[0].last_name} : '
                #'(1 pour gagner, 0 perdu, 0.5 pour égalité) : '))
                if result_one == 0:
                    result_two = 1
                    break
                elif result_one == 1:
                    result_two = 0
                    break
                elif result_one == 0.5:
                    result_two = 0.5
                    break
                else:
                    print('Veuillez inscrire un score de 0, 1 ou 0.5')
            except ValueError:
                print('Vous n\'avez pas inscrit un chiffre.')
        
        results.append(result_one)
        results.append(result_two)
        players = players[2:]
        i += 1
    
    return results


def create_match_list(results, players):
    """Créer une liste de matchs contenant des joueurs et des scores."""
    match_list = []
    while results != []:
        l1 = [players[0], results[0]]
        l2 = [players[1], results[1]]
        match = (l1, l2)
        match_list.append(match)
        players = players[2:]
        results = results[2:]
    
    return match_list

        