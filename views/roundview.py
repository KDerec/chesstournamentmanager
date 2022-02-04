from views import userinput


def start_round(self):
    print(f'Commencer le tour {self+1} ?')

    return userinput.input_choice()


def end_round(self):
    print(f'Terminer le tour {self+1} ?')

    return userinput.input_choice()

def display_first_round_versus(i, top_players, low_players):
    print(f'Match #{i+1} : '
    f'{top_players[i].first_name} {top_players[i].last_name} {top_players[i].rank} vs '
    f'{low_players[i].first_name} {low_players[i].last_name} {low_players[i].rank} (joue en blanc).')


def display_other_round_versus(i, p1, d1):
    print(f'Match #{i+1} : '
        f'{p1[i].first_name} {p1[i].last_name} ({d1[p1[i]]}) vs '
        f'{p1[i+1].first_name} {p1[i+1].last_name} ({d1[p1[i+1]]}) (joue en blanc).')


def display_players_already_played_together(player_one, player_two):
    print(f'{player_one.last_name} à déjà joué avec {player_two.last_name}.')