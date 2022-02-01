import datetime
from datetime import timedelta
from controllers import errorcontroller
from controllers import playercontroller
from models.database import Database
from views.message import errormessage
from views.input.tournamentinput import InputTournament
from views.input import menuinput


def prepare_tournament_attributs():
    """Préparation des attributs du tournoi."""
    tournament = InputTournament()
    while True:
        try:
            if tournament.name != False:
                pass
            else:
                tournament.input_name()
            if tournament.name == '':
                tournament.name = False
                raise errorcontroller.EmptyInputException
            
            if tournament.location != False:
                pass
            else:
                tournament.input_location()
            if tournament.location == '':
                tournament.location = False
                raise errorcontroller.EmptyInputException
            
            if tournament.time_controller != False:
                pass
            else:
                selected_mode = tournament.input_mode()
            if selected_mode in range(len(tournament.mode)):
                tournament.time_controller = tournament.mode[selected_mode]
            else:
                raise errorcontroller.ModeOutOfRangeException
            
            if tournament.duration != False:
                pass
            else:
                tournament.input_duration()
            if tournament.duration <= 0:
                tournament.duration = False
                raise errorcontroller.NotPositiveIntegerException
            
            if tournament.number_of_rounds != False:
                pass
            else:
                tournament.input_number_of_rounds()
            if tournament.number_of_rounds <= 0:
                tournament.number_of_rounds = False
                raise errorcontroller.NotPositiveIntegerException
            
            if tournament.description != False:
                pass
            else:
                tournament.input_description()

            tournament.display_summary()

            validation = tournament.validate_creation()

            if validation:
                if tournament.duration > 1:
                    first_day = datetime.date.today()
                    last_day = (first_day + timedelta(days=(
                                                    tournament.duration-1)))
                    tournament.date = (str(first_day) + '_' + str(last_day))
                else:
                    tournament.date = str(datetime.date.today())
                
                return tournament
                
                
            else:
                delete_all_attribut(tournament)
                break


        except ValueError:
            errormessage.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errormessage.display_its_blank_message()
        except errorcontroller.ModeOutOfRangeException:
            errormessage.display_not_in_mode_range()
        except errorcontroller.NotPositiveIntegerException:
            errormessage.display_not_positive_integer()


def delete_all_attribut(self):
    list_to_delete = []
    for attribut in vars(self):
        if not attribut.startswith('_'):
            list_to_delete.append(attribut)
           
    for attribut in list_to_delete:
        delattr(self, attribut)

def prepare_tournament():
    tournament = prepare_tournament_attributs()
    if tournament:
        for i in range(12):
            playercontroller.create_player()
        
        while True:
            try:
                number_of_player = menuinput.input_number_of_player_in_tournament()
                break
            except ValueError:
                errormessage.display_not_an_integer_message()
        Database.dispay_player_in_database(Database)
        while len(tournament.players_list) != number_of_player:
            try:
                player_number = menuinput.input_player_number()
                tournament.add_player_in_players_list(
                                Database.player_database[player_number])

            except ValueError:
                errormessage.display_not_an_integer_message()
            except IndexError:
                errormessage.display_wrong_choice_message()
        
        tournament.dispay_player_in_tournament()
        