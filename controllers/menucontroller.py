# import os
# import sys
# mydir = os.getcwd()
# sys.path.append(mydir)
import time
import models
from controllers import playercontroller
from controllers import tournamentcontroller
from views.message import menumessage
from views.message import errormessage
from models.database import Database



def run():
    running = True
    while running:
        try:
            choice = menumessage.display_main_menu()
            
            if choice == 1:
                while True:
                    try:
                        choice = menumessage.display_tournament_menu()
                        if choice == 1:
                            tournamentcontroller.prepare_tournament()

                        elif choice == 2:
                            break
                        else:
                            errormessage.display_wrong_choice_message()
                    except ValueError:
                        errormessage.display_not_an_integer_message()
            
            elif choice == 2:
                while True:
                    try:
                        choice = menumessage.display_player_menu()
                        if choice == 1:
                            playercontroller.create_player()
                        elif choice == 2:
                            print('Afficher suppression de joueur')
                        elif choice == 3:
                            break
                        else:
                            errormessage.display_wrong_choice_message()
                    except ValueError:
                        errormessage.display_not_an_integer_message()
            
            elif choice == 3:
                while True:
                    try:
                        choice = menumessage.display_report_menu()
                        if choice == 1:
                            print('Affiche rapport.')
                        elif choice == 2:
                            print('Export rapport.')
                        elif choice == 3:
                            break
                        else:
                            errormessage.display_wrong_choice_message()
                    except ValueError:
                        errormessage.display_not_an_integer_message()

            elif choice == 4:
                choice = menumessage.display_exit_message()
                if choice.upper() == 'Q':
                    running = False
            else:
                errormessage.display_wrong_choice_message()
        except ValueError:
            errormessage.display_not_an_integer_message()
    exit()




def create_round(i):
    '''Préparation des attributs d'un tour.'''
    name = f'Round {i+1}'
    beginning_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))
    ending_date = ''
    round = Round(name, beginning_date, ending_date)

    return round

def select_random_player_in_database(self):
    '''Simule le choix de 8 joueurs dans la base de données.'''
    return random.sample(self, 8)

def generate_players_database():
    players_database = []

    for i in range(24):
        player = create_player()
        players_database.append(player)
    
    return players_database

if __name__ == "__main__":
    run()