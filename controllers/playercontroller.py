import datetime
from controllers import errorcontroller
from views.message import errormessage
from views.input.playerinput import PlayerInput, PlayerInputAuto
from models.database import Database

def create_player():
    player = PlayerInputAuto()
    while True:
        try:
            if player.last_name != False:
                pass
            else:
                player.input_last_name()
            if player.last_name == '':
                player.last_name = False
                raise errorcontroller.EmptyInputException
            elif has_numbers(player.last_name):
                player.last_name = False
                raise errorcontroller.HasNumberException
            
            if player.first_name != False:
                pass
            else:
                player.input_first_name()
            if player.first_name == '':
                player.first_name = False
                raise errorcontroller.EmptyInputException
            elif has_numbers(player.first_name):
                player.first_name = False
                raise errorcontroller.HasNumberException
            
            if player.birthday != False:
                pass
            else:
                day = player.input_birthday_day()
                if day <= 0:
                    raise errorcontroller.NotPositiveIntegerException
                elif day >= 32:
                    raise errorcontroller.ImpossibleBirthdayDateException
                month = player.input_birthday_month()
                if month <= 0:
                    raise errorcontroller.NotPositiveIntegerException
                elif month > 12:
                    raise errorcontroller.ImpossibleBirthdayDateException
                year = player.input_birthday_year()
                if year <= 0:
                    raise errorcontroller.NotPositiveIntegerException
                elif year < 1900 or year > (datetime.date.today().year - 16):
                    raise errorcontroller.ImpossibleBirthdayDateException
                player.birthday = datetime.date(year, month, day)


            if player.sexe != False:
                pass
            else:
                selected_sexe = player.input_sexe()
            if selected_sexe in range(len(player.possible_sexe)):
                player.sexe = player.possible_sexe[selected_sexe]
            else:
                raise errorcontroller.ModeOutOfRangeException
            
            if player.rank != False:
                pass
            else:
                player.input_rank()
            if player.rank < 0:
                player.rank = False
                raise errorcontroller.NotPositiveIntegerException

            player.display_summary()

            validation = player.validate_creation()

            if validation:
                database = Database()
                database.add_player_in_database(player)
                break
                
            else:
                break


        except ValueError:
            errormessage.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errormessage.display_its_blank_message()
        except errorcontroller.ModeOutOfRangeException:
            errormessage.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errormessage.display_not_positive_integer()
        except errorcontroller.ImpossibleBirthdayDateException:
            errormessage.display_not_possible_birthday_date()
        except errorcontroller.HasNumberException:
            errormessage.display_has_a_number()

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)