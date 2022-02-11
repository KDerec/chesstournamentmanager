"""Define database."""


import os
from tinydb import TinyDB


class Database:

    mydir = os.getcwd()
    db = TinyDB(mydir + '\data\db.json')
    player_table = db.table('player_table')
    tournament_table = db.table('tournament_table')

    def __init__(self):
        pass

    def dispay_player_in_database(self):
        for player in self.player_table:
            print(player.doc_id, player['last_name'], player['first_name'], player['rank'])
    
    def insert_player_in_table(self, player):        
        self.player_table.insert(player)

    def insert_tournament_in_table(self, tournament):        
        self.tournament_table.insert(tournament)
