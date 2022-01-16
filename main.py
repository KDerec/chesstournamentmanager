from bin.tournament import create_tournament
from bin.player import create_player


def main():
    tournament = create_tournament()
    for i in range(8):
        player = create_player()
        tournament.add_player_in_players_list(player)


if __name__ == "__main__":
    main()