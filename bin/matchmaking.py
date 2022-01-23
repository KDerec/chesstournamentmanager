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
        d1 = {}
        for i in range(len(tournament.players_list)):
            d1[tournament.players_list[i]] = 0
        for i in range(len(tournament.rounds_list)):
            for j in range(len(tournament.rounds_list[i].match_list)):
                player_one = tournament.rounds_list[i].match_list[j][0][0]
                player_two = tournament.rounds_list[i].match_list[j][1][0]
                score_one = tournament.rounds_list[i].match_list[j][0][1]
                score_two = tournament.rounds_list[i].match_list[j][1][1]
                d1[player_one] += score_one
                d1[player_two] += score_two
        
        d1 = dict(sorted(d1.items(), key=lambda item: item[1], reverse=True))
        d2 = dict(d1)
        l1 = list(d2)

        while d2 != {}:
            temp_list = []
            try:
                temp_list.append(l1[0])
            except IndexError:
                break
            for player in l1:
                if d2[temp_list[0]] == d2[player]:
                    if player in temp_list:
                        continue
                    else:
                        temp_list.append(player)
                    
                    del d2[player]

            temp_list = sorted(temp_list, key=lambda player: player.rank, 
                                reverse=True)
        
            for player in temp_list:
                player_matchmaking.append(player)
                l1.remove(player)

            i += 1

        if end == True:
            return d1, player_matchmaking
        else:
            for i in range(len(tournament.rounds_list)):
                for j in range(len(tournament.rounds_list[i].match_list)):
                    player_one = tournament.rounds_list[i].match_list[j][0][0]
                    player_two = tournament.rounds_list[i].match_list[j][1][0]

                    if (player_one == player_matchmaking[0] and 
                        player_two == player_matchmaking[1]):
                        print(f'{player_one.last_name} à déjà joué avec '
                              f'{player_two.last_name}')
                        player_matchmaking[1], player_matchmaking[2] = (
                        player_matchmaking[2], player_matchmaking[1])
            
            p1 = player_matchmaking
            for i in range(len(p1) // 2):
                print(f'Match #{i+1} : '
                f'{p1[i].first_name} {p1[i].last_name} ({d1[p1[i]]}) vs '
                f'{p1[i+1].first_name} {p1[i+1].last_name} ({d1[p1[i+1]]})')
                p1 = p1[1:]

            return player_matchmaking
      