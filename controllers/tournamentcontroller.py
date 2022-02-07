import datetime
from datetime import timedelta
from models.database import Database
from controllers import errorcontroller
from controllers import playercontroller
from controllers import roundcontroller
from controllers import matchcontroller
from controllers import systemcontroller
from views import errorview
from views import tournamentview
from views import playerview
from views import roundview
from views.tournamentinput import InputTournament


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
                choice = tournamentview.change_the_number_of_rounds()
                if systemcontroller.choice_verification(choice):
                    tournament.input_number_of_rounds()
                else:
                    tournament.number_of_rounds = 4
            if tournament.number_of_rounds <= 0:
                tournament.number_of_rounds = False
                raise errorcontroller.NotPositiveIntegerException
            
            if tournament.description != False:
                pass
            else:
                choice = tournamentview.add_a_description()
                if systemcontroller.choice_verification(choice):
                    tournament.input_description()
                else:
                    tournament.description = ''

            tournament.display_summary()

            choice = tournamentview.validate_creation()

            if systemcontroller.choice_verification(choice):
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
            errorview.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errorview.display_its_blank_message()
        except errorcontroller.ModeOutOfRangeException:
            errorview.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()


def prepare_tournament():
    tournament = prepare_tournament_attributs()
    if tournament:
        # Ceci sera réalisé par l'utilisateur.
        for i in range(12):
            playercontroller.create_player()
        
        select_player_to_add_in_tournament(tournament)
        tournamentview.display_start_tournament()
        start_tournament(tournament)


def select_player_to_add_in_tournament(tournament):
    while True:
        try:
            number_of_player = tournamentview.how_many_player_will_play()
            if number_of_player % 2 != 0:
                raise errorcontroller.NotAnEvenNumberException
            if number_of_player > len(Database.player_database):
                raise errorcontroller.NotEnoughPlayerInDatabaseException
            break
        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.NotAnEvenNumberException:
            errorview.display_not_an_even_number()
        except errorcontroller.NotEnoughPlayerInDatabaseException:
            errorview.display_you_selected_too_much_player()

    Database.dispay_player_in_database(Database)
    selected_player = []

    while len(tournament.players_list) != number_of_player:
        try:
            player_number = tournamentview.wich_player_will_play()
            if player_number in selected_player:
                raise errorcontroller.WrongChosenPlayerException
            else:
                selected_player.append(player_number)
                tournament.add_player_in_players_list(
                                Database.player_database[player_number])

        except ValueError:
            errorview.display_not_an_integer_message()
        except IndexError:
            errorview.display_wrong_choice_message()
        except errorcontroller.WrongChosenPlayerException:
            errorview.display_this_player_is_already_chosen()
    
    tournament.display_player_in_tournament()

    choice = tournamentview.validate_chosen_players()

    if systemcontroller.choice_verification(choice):
        pass
        
    else:    
        tournament.players_list = []
        select_player_to_add_in_tournament(tournament)


def start_tournament(tournament):
    for i in range(tournament.number_of_rounds):
        propose_to_change_player_rank(tournament)
        while True:
            choice = roundview.start_round(i)
            if systemcontroller.choice_verification(choice):
                round = roundcontroller.create_round(i)
                round.display_round_name()
                players_matchmaking = roundcontroller.play_round(round, tournament)
                break

        while True:
            propose_to_change_player_rank(tournament)
            choice = roundview.end_round(i)
            if systemcontroller.choice_verification(choice):
                roundcontroller.create_ending_round_date(round)
                results = matchcontroller.create_match_results(players_matchmaking)
                match_list = matchcontroller.create_match_list(results, players_matchmaking)
                round.match_list = match_list
                tournament.add_round_in_rounds_list(round)
                break
    
    propose_to_change_player_rank(tournament)
    prepare_standings(round, tournament)


def prepare_standings(round, tournament):
    player_matchmaking, classement = roundcontroller.play_round(round, tournament, end = True)
    print('\nLes résultats du tournoi sont : ')
    for i in range(len(classement)):
        tournamentview.display_standings(player_matchmaking, classement, i)


def propose_to_change_player_rank(tournament):
    choice = playerview.change_player_rank()
    if systemcontroller.choice_verification(choice):
        select_player_to_change_his_rank(tournament)

def select_player_to_change_his_rank(tournament):
    tournament.display_player_in_tournament()
    while True:
        try:
            selected_player = playerview.select_a_player_to_change_his_rank()
            new_rank = playerview.choice_new_rank()
            if new_rank < 0:
                raise errorcontroller.NotPositiveIntegerException
            tournament.players_list[selected_player].update_player_rank(new_rank)
            break
        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()
    