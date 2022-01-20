import time
from bin.matchmaking import matchmaking
from bin.tournament import create_tournament
from bin.player import create_player, select_random_player_in_database
from bin.round import create_round
from bin.match import create_match_results
from bin.match import create_match_list

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
            player_matchmaking = matchmaking(round, tournament)
            choice = 'O' #input(f'Terminer le tour {i+1} ? Oui = o')
            if choice.upper() == 'O':
                round.ending_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))
                results = create_match_results(player_matchmaking)
                match_list = create_match_list(results, player_matchmaking)
                round.match_list = match_list
                tournament.add_round_in_rounds_list(round)
    
    classement, player_matchmaking = matchmaking(round, tournament, end = True)
    print('\nLes résultats du tournoi sont : ')
    for i in range(len(classement)):
        print(f'{i+1}# avec {classement[player_matchmaking[i]]} points: '
        f'{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}')
        
                

if __name__ == "__main__":
    main()