"""Define database."""


import os
from tinydb import TinyDB


class Database:
    player_database = []

    def __init__(self):
        pass

    def add_player_in_database(self, player):
        self.player_database.append(player)

    def dispay_player_in_database(self):
        for player in self.player_database:
            print(f'{self.player_database.index(player)}. {player.last_name} {player.first_name} ({player.rank})')
    
    def create_database():
        mydir = os.getcwd()
        TinyDB(mydir + '\data\db.json')

        return TinyDB(mydir + '\data\db.json')

    def create_player_table(db):        
        return db.table('player_table')

    def create_tournament_table(db):        
        return db.table('tournament_table')
