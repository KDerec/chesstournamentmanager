from bin.tournament import create_tournament
from bin.player import create_player, select_random_player_in_database

def main():
    database_players = []
    tournament = create_tournament()
    
    for i in range(24):
        player = create_player()
        database_players.append(player)

    chosen_player = select_random_player_in_database(database_players)

    for i in range(len(chosen_player)):
        tournament.add_player_in_players_list(chosen_player[i])

if __name__ == "__main__":
    main()