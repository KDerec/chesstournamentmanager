import datetime
from datetime import timedelta
from models.database import Database
from controllers import errorcontroller
from controllers import playercontroller
from controllers import roundcontroller
from controllers import matchmakingcontroller
from controllers import matchcontroller
from views.message import errormessage
from views.message import menumessage
from views.input.tournamentinput import InputTournament


def prepare_tournament_attributs():
    """Préparation des attributs du tournoi."""
    tournament = InputTournament()
    running = True
    while running:
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
                running = False


        except ValueError:
            errormessage.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errormessage.display_its_blank_message()
        except errorcontroller.ModeOutOfRangeException:
            errormessage.display_not_in_mode_range()
        except errorcontroller.NotPositiveIntegerException:
            errormessage.display_not_positive_integer()


def prepare_tournament():
    tournament = prepare_tournament_attributs()
    if tournament:
        # Ceci sera réalisé par l'utilisateur.
        for i in range(12):
            playercontroller.create_player()
        
        select_player_to_add_in_tournament(tournament)
        menumessage.display_ready_to_start_tournament()
        start_tournament(tournament)

def select_player_to_add_in_tournament(self):
    while True:
        try:
            number_of_player = menumessage.display_how_many_player_will_play()
            break
        except ValueError:
            errormessage.display_not_an_integer_message()

    Database.dispay_player_in_database(Database)
    selected_player = []

    while len(self.players_list) != number_of_player:
        try:
            player_number = menumessage.display_wich_player_will_play()
            if player_number in selected_player:
                raise errorcontroller.WrongChosenPlayer
            else:
                selected_player.append(player_number)
                self.add_player_in_players_list(
                                Database.player_database[player_number])

        except ValueError:
            errormessage.display_not_an_integer_message()
        except IndexError:
            errormessage.display_wrong_choice_message()
        except errorcontroller.WrongChosenPlayer:
            errormessage.display_this_player_is_already_chosen()
    
    self.dispay_player_in_tournament()

    choice = menumessage.display_validate_chosen_players()

    if choice.upper() != 'O':
        self.players_list = []
        select_player_to_add_in_tournament(self)


def start_tournament(self):
    for i in range(self.number_of_rounds):
        while True:
            choice = menumessage.display_start_round(i)
            if choice.upper() == 'O':
                round = roundcontroller.create_round(i)
                round.display_round_name()
                player_matchmaking = matchmakingcontroller.matchmaking(round, self)
                break

        while True:
            choice = menumessage.display_end_round(i)
            if choice.upper() == 'O':
                roundcontroller.create_ending_round_date(round)
                results = matchcontroller.create_match_results(player_matchmaking)
                match_list = matchcontroller.create_match_list(results, player_matchmaking)
                round.match_list = match_list
                self.add_round_in_rounds_list(round)
                break