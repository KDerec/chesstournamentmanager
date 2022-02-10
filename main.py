from models.database import Database
from controllers import menucontroller, tournamentcontroller


def main():
    db = Database.create_database()
    player_table = Database.create_player_table(db)
    tournament_table = Database.create_tournament_table(db)
    tournament_table.insert({'2': 'test'})
    menucontroller.run()


if __name__ == "__main__":
    main()