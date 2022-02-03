""""Définit un match."""

import random
from views.message import menumessage
from views.message import errormessage

def create_match_results(self):
    """Créer une liste de score."""
    i = 1
    results = []
    players = self
    while players != []:
        menumessage.display_match_notation(i, players)
        while True:
            try:
                result_one = menumessage.display_note_the_match(players) # random.choice([0,0.5,1])
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
                    errormessage.display_wrong_choice_message()
            except ValueError:
                errormessage.display_not_an_integer_or_float_number()
        
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

        