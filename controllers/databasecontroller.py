from models.database import Database
from models.encoder import encode_class_to_dict


def insert_player_in_db(player):
    player = encode_class_to_dict(player)
    db = Database()
    db.insert_player_in_table(player)
