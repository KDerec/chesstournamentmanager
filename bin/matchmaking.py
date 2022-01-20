"""Définit le jumelage des joueurs."""


def split_list(self):
    '''Divise une liste en deux.'''
    half = len(self) // 2
    return self[:half], self[half:]

def matchmaking(round, tournament, end = False):
    """Génére le jumelage de joueur."""
    player_matchmaking = []
    if round.name == 'Round 1':
        sorted_list = sorted(tournament.players_list, 
                                        key=lambda player: player.rank,
                                        reverse=True)
        top_players, low_players = split_list(sorted_list)

        for i in range(len(top_players)):
            print(f'Match #{i+1} : '
            f'{top_players[i].first_name} {top_players[i].last_name} vs '
            f'{low_players[i].first_name} {low_players[i].last_name}')

            player_matchmaking.append(top_players[i])
            player_matchmaking.append(low_players[i])

        return player_matchmaking
    
    else:
        return [1,2,3,4]