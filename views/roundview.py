"""Display round messages."""


from views import userinput


def start_round(self):
    """Display start round number and return user choice."""
    print(f'Commencer le tour {self+1} ?')

    return userinput.input_choice()


def end_round(self):
    """Display end round number and return user choice."""

    print(f'Terminer le tour {self+1} ?')

    return userinput.input_choice()


def display_first_round_versus(i, top_players, low_players):
    """Display first round versus."""

    print(f'Match #{i+1} : '
    f'{top_players[i].first_name} {top_players[i].last_name} {top_players[i].rank} vs '
    f'{low_players[i].first_name} {low_players[i].last_name} {low_players[i].rank} (joue en blanc).')


def display_other_round_versus(i, p1, d1):
    """Display other round versus."""

    print(f'Match #{i+1} : '
        f'{p1[i].first_name} {p1[i].last_name} ({d1[p1[i]]}) vs '
        f'{p1[i+1].first_name} {p1[i+1].last_name} ({d1[p1[i+1]]}) (joue en blanc).')


def display_players_already_played_together(player_one, player_two):
    """Display players already play together."""
    
    print(f'{player_one.last_name} à déjà joué avec {player_two.last_name}.')