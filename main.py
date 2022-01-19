import time
from bin.tournament import create_tournament
from bin.player import create_player, select_random_player_in_database
from bin.round import create_round

def main():
    database_players = []
    tournament = create_tournament()
    
    for i in range(24):
        player = create_player()
        database_players.append(player)

    chosen_player = select_random_player_in_database(database_players)

    for i in range(len(chosen_player)):
        tournament.add_player_in_players_list(chosen_player[i])
        
    for i in range(tournament.number_of_rounds):
        choice = 'O' #input(f'Commencer le tour {i+1} ? Oui = o')
        if choice.upper() == 'O':
            round = create_round(i)
            choice = 'O' #input(f'Terminer le tour {i+1} ? Oui = o')
            if choice.upper() == 'O':
                round.ending_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))

if __name__ == "__main__":
    main()