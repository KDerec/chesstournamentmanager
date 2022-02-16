"""Manage creation of player object."""


import datetime
from controllers import databasecontroller
from controllers import errorcontroller
from controllers import systemcontroller
from views import errorview
from views import playerview
from views.playerinput import PlayerInput


def create_player():
    """Input player attributs and return player object."""
    player = PlayerInput()
    while True:
        try:
            if player.last_name is not False:
                pass
            else:
                player.input_last_name()
            if player.last_name == "":
                player.last_name = False
                raise errorcontroller.EmptyInputException
            elif has_numbers(player.last_name):
                player.last_name = False
                raise errorcontroller.HasNumberException

            if player.first_name is not False:
                pass
            else:
                player.input_first_name()
            if player.first_name == "":
                player.first_name = False
                raise errorcontroller.EmptyInputException
            elif has_numbers(player.first_name):
                player.first_name = False
                raise errorcontroller.HasNumberException

            if player.birthday is not False:
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
                player.birthday = str(datetime.date(year, month, day))

            if player.sexe is not False:
                pass
            else:
                selected_sexe = player.input_sexe()
            if selected_sexe in range(len(player.possible_sexe)):
                player.sexe = player.possible_sexe[selected_sexe]
            else:
                raise errorcontroller.OutOfRangeException

            if player.rank is not False:
                pass
            else:
                player.input_rank()
            if player.rank < 0:
                player.rank = False
                raise errorcontroller.NotPositiveIntegerException

            player.display_summary()

            choice = playerview.validate_creation()

            if systemcontroller.choice_verification(choice):
                databasecontroller.insert_player_in_db(player)
                break

            else:
                break

        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errorview.display_its_blank_message()
        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()
        except errorcontroller.ImpossibleBirthdayDateException:
            errorview.display_not_possible_birthday_date()
        except errorcontroller.HasNumberException:
            errorview.display_has_a_number()


def has_numbers(inputString):
    """Check if there is a number in a string list and return True or False."""
    return any(char.isdigit() for char in inputString)
