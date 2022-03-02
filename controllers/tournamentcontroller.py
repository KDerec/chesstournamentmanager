"""Manage the running of a tournament."""


import datetime
from datetime import timedelta
from models.database import Database as db
from models.encoder import encode_json_to_dict
from models.player import DictToPlayer
from models.tournament import DictToTournament
from models.round import DictToRound
from controllers import errorcontroller
from controllers import roundcontroller
from controllers import matchcontroller
from controllers import systemcontroller
from controllers import databasecontroller
from controllers import playercontroller
from views import errorview
from views import matchview
from views import tournamentview
from views import playerview
from views import roundview
from views import databaseview
from views.tournamentinput import InputTournament


def prepare_tournament_attributs():
    """Input tournament attributs and return tournament object."""
    tournament = InputTournament()
    running = True
    while running:
        try:
            if tournament.name is not False:
                pass
            else:
                tournament.input_name()
            if tournament.name == "":
                tournament.name = False
                raise errorcontroller.EmptyInputException

            if tournament.location is not False:
                pass
            else:
                tournament.input_location()
            if tournament.location == "":
                tournament.location = False
                raise errorcontroller.EmptyInputException

            if tournament.time_controller is not False:
                pass
            else:
                selected_mode = tournament.input_mode()
            if selected_mode in range(len(tournament.mode)):
                tournament.time_controller = tournament.mode[selected_mode]
            else:
                raise errorcontroller.OutOfRangeException

            if tournament.duration is not False:
                pass
            else:
                tournament.input_duration()
            if tournament.duration <= 0:
                tournament.duration = False
                raise errorcontroller.NotPositiveIntegerException

            if tournament.number_of_rounds is not False:
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

            if tournament.description is not False:
                pass
            else:
                choice = tournamentview.add_a_description()
                if systemcontroller.choice_verification(choice):
                    tournament.input_description()
                else:
                    tournament.description = ""

            tournament.display_summary()

            choice = tournamentview.validate_creation()

            if systemcontroller.choice_verification(choice):
                if tournament.duration > 1:
                    first_day = datetime.date.today()
                    last_day = first_day + timedelta(days=(tournament.duration - 1))
                    tournament.date = str(first_day) + "_" + str(last_day)
                else:
                    tournament.date = str(datetime.date.today())

                delattr(tournament, "duration")

                return tournament

            else:
                running = False

        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errorview.display_its_blank_message()
        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()


def call_players_selection_and_start_tournament():
    """Select player to add in tournament and call start_tournament function."""
    tournament = prepare_tournament_attributs()
    if tournament:
        select_player_to_add_in_tournament(tournament)
        tournamentview.display_start_tournament()
        databasecontroller.insert_tournament_in_db(tournament)
        start_tournament(tournament)


def select_player_to_add_in_tournament(tournament):
    """Select how many players will play and add players in tournament object."""
    while True:
        try:
            number_of_player = tournamentview.how_many_player_will_play()
            if number_of_player % 2 != 0:
                raise errorcontroller.NotAnEvenNumberException
            if number_of_player > len(db.player_table):
                raise errorcontroller.NotEnoughPlayerInDatabaseException
            if number_of_player < 4:
                raise errorcontroller.NumberOfPlayerIsTooLow
            break
        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.NotAnEvenNumberException:
            errorview.display_not_an_even_number()
        except errorcontroller.NotEnoughPlayerInDatabaseException:
            errorview.display_you_selected_too_much_player()
        except errorcontroller.NumberOfPlayerIsTooLow:
            errorview.display_not_enough_player()

    databaseview.display_player_in_db()
    selected_player = []

    while len(tournament.players_list) != number_of_player:
        try:
            player_number = tournamentview.wich_player_will_play()
            if player_number in selected_player:
                raise errorcontroller.WrongChosenPlayerException
            if player_number > len(db.player_table) or player_number <= 0:
                raise errorcontroller.OutOfRangeException
            else:
                selected_player.append(player_number)
                player = db.player_table.get(doc_id=player_number)
                player = encode_json_to_dict(player)
                player = DictToPlayer(player)
                tournament.add_player_in_players_list(player)

        except ValueError:
            errorview.display_not_an_integer_message()
        except IndexError:
            errorview.display_wrong_choice_message()
        except errorcontroller.WrongChosenPlayerException:
            errorview.display_this_player_is_already_chosen()
        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()

    tournament.display_player_in_tournament()

    choice = tournamentview.validate_chosen_players()

    if systemcontroller.choice_verification(choice):
        pass

    else:
        tournament.players_list = []
        select_player_to_add_in_tournament(tournament)


def start_tournament(tournament):
    """Run tournament until each rounds are played."""
    if len(tournament.rounds_list) > 0:
        round_number = len(tournament.rounds_list)
    else:
        round_number = 0
    while len(tournament.rounds_list) < tournament.number_of_rounds:
        propose_to_change_player_rank(tournament)
        while True:
            choice = roundview.start_round(round_number)
            if systemcontroller.choice_verification(choice):
                round = roundcontroller.create_round(round_number)
                round.display_round_name()
                players_matchmaking = roundcontroller.play_round(round, tournament)
                databasecontroller.update_tournament_in_db(tournament)
                break

        while True:
            propose_to_change_player_rank(tournament)
            choice = roundview.end_round(round_number)
            if systemcontroller.choice_verification(choice):
                roundcontroller.create_ending_round_date(round)
                while True:
                    results = matchcontroller.create_match_results(players_matchmaking)
                    choice = matchview.validate_match_result()
                    if systemcontroller.choice_verification(choice):
                        break
                match_list = matchcontroller.create_match_list(results, players_matchmaking)
                round.match_list = match_list
                tournament.add_round_in_rounds_list(round)
                databasecontroller.update_tournament_in_db(tournament)
                round_number += 1
                break

    propose_to_change_player_rank(tournament)
    prepare_standings(round, tournament)
    databasecontroller.update_tournament_in_db(tournament)


def prepare_standings(round, tournament):
    """Prepare standings for the end of the tournament."""
    player_matchmaking, classement = roundcontroller.play_round(round, tournament, end=True)
    print("\nLes résultats du tournoi sont : ")
    for i in range(len(classement)):
        tournamentview.display_standings(player_matchmaking, classement, i)


def propose_to_change_player_rank(tournament):
    """Ask for player rank change."""
    choice = playerview.change_player_rank()
    if systemcontroller.choice_verification(choice):
        select_player_to_change_his_rank(tournament)


def select_player_to_change_his_rank(tournament):
    """Select a player in tournament and input new rank."""
    tournament.display_player_in_tournament()
    while True:
        try:
            selected_player = playerview.select_a_player_to_change_his_rank()
            new_rank = playerview.choice_new_rank()
            if new_rank < 0:
                raise errorcontroller.NotPositiveIntegerException
            databasecontroller.update_player_rank_in_db(tournament.players_list[selected_player], new_rank)
            tournament.players_list[selected_player].update_player_rank(new_rank)
            break
        except ValueError:
            choice = tournamentview.return_in_tournament()
            if systemcontroller.choice_verification(choice):
                break
            errorview.display_not_an_integer_message()
        except IndexError:
            errorview.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()


def check_if_a_tournament_is_not_over():
    """Compare number of round and round list and ask for user answer."""
    for tournament in db.tournament_table:
        if len(tournament["rounds_list"]) < tournament["number_of_rounds"]:
            choice = tournamentview.tournament_is_not_over(tournament)

            if systemcontroller.choice_verification(choice):
                prepare_tournament_to_restart(tournament)


def prepare_tournament_to_restart(tournament):
    tournament = encode_json_to_dict(tournament)
    tournament = DictToTournament(tournament)
    players_list_in_class_format = []
    for player in tournament.players_list:
        player = DictToPlayer(player)
        players_list_in_class_format.append(player)
    delattr(tournament, "players_list")
    tournament.players_list = players_list_in_class_format

    rounds_list_in_class_format = []
    for round in tournament.rounds_list:
        round = DictToRound(round)
        rounds_list_in_class_format.append(round)
    delattr(tournament, "rounds_list")
    tournament.rounds_list = rounds_list_in_class_format
    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_one = playercontroller.found_corresponding_player_object_in_list(tournament, player_one)
            del tournament.rounds_list[i].match_list[j][0][0]
            tournament.rounds_list[i].match_list[j][0].insert(0, player_one)

            player_two = tournament.rounds_list[i].match_list[j][1][0]
            player_two = playercontroller.found_corresponding_player_object_in_list(tournament, player_two)
            del tournament.rounds_list[i].match_list[j][1][0]
            tournament.rounds_list[i].match_list[j][1].insert(0, player_two)

    start_tournament(tournament)
