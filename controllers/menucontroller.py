# import os
# import sys
# mydir = os.getcwd()
# sys.path.append(mydir)
from controllers import playercontroller
from controllers import tournamentcontroller
from views.message import menumessage
from views.message import errormessage


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


if __name__ == "__main__":
    run()