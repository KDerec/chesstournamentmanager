"""Define database."""


import os
from tinydb import TinyDB, Query


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

    def update_player_rank_in_table(self, player, new_rank):
        player_in_db = self.player_table.get(
                        (Query().last_name == player.last_name) &
                        (Query().first_name == player.first_name) &
                        (Query().birthday == player.birthday) &
                        (Query().sexe == player.sexe) &
                        (Query().rank == player.rank))
        self.player_table.update({'rank': new_rank}, doc_ids=[player_in_db.doc_id])
