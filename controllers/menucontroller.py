"""Where the user navigate between each menus."""


from controllers import playercontroller
from controllers import tournamentcontroller
from controllers import systemcontroller
from controllers import reportingcontroller
from views import menuview
from views import errorview


def run():
    """Navigate in menus."""
    
    running = True
    while running:
        try:
            choice = menuview.display_main_menu()
            
            if choice == 1:
                while True:
                    try:
                        choice = menuview.display_tournament_menu()
                        if choice == 1:
                            tournamentcontroller.call_players_selection_and_start_tournament()

                        elif choice == 2:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()
            
            elif choice == 2:
                while True:
                    try:
                        choice = menuview.display_player_menu()
                        if choice == 1:
                            playercontroller.create_player()
                        elif choice == 2:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()
            
            elif choice == 3:
                while True:
                    try:
                        choice = menuview.display_report_menu()
                        if choice == 1:
                            reportingcontroller.display_reporting()
                        elif choice == 2:
                            print('Export rapport.')
                        elif choice == 3:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 4:
                systemcontroller.exit_application()
            else:
                errorview.display_wrong_choice_message()
        except ValueError:
            errorview.display_not_an_integer_message()
