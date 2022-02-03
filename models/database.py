

class Database:
    player_database = []

    def __init__(self):
        pass

    def add_player_in_database(self, player):
        self.player_database.append(player)

    def dispay_player_in_database(self):
        for player in self.player_database:
            print(f'{self.player_database.index(player)}. {player.last_name} {player.first_name} ({player.rank})')