"""Manage the running of a round."""


import time
from models.round import Round
from views import roundview


def create_round(i):
    """Create round attributs and return a round object."""
    name = f"Round {i+1}"
    beginning_date = "{}".format(time.strftime("%Y-%m-%d_%Hh"))
    ending_date = ""
    round = Round(name, beginning_date, ending_date)

    return round


def create_ending_round_date(self):
    """Create ending date and update ending date round object attribut."""
    self.ending_date = "{}".format(time.strftime("%Y-%m-%d_%Hh"))


def split_list(self):
    """Divide a list by two and return two lists."""
    half = len(self) // 2
    return self[:half], self[half:]


def play_round(round, tournament, end=False):
    """Check the round number and call matchmaking functions according."""
    if round.name == "Round 1":
        return matchmaking_for_first_round(tournament)

    else:
        return matchmaking_for_others_round(tournament, end)


def matchmaking_for_first_round(tournament):
    """Create matchmaking for first round and return a sorted player list."""
    players_matchmaking = []
    sorted_list = sorted(tournament.players_list, key=lambda player: player.rank, reverse=True)
    top_players, low_players = split_list(sorted_list)

    for i in range(len(top_players)):
        roundview.display_first_round_versus(i, top_players, low_players)
        players_matchmaking.append(top_players[i])
        players_matchmaking.append(low_players[i])

    return players_matchmaking


def matchmaking_for_others_round(tournament, end):
    """Create matchmaking and return a sorted player list."""
    players_matchmaking = []
    players_and_scores = {}

    for i in range(len(tournament.players_list)):
        players_and_scores[tournament.players_list[i]] = 0

    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_two = tournament.rounds_list[i].match_list[j][1][0]
            score_one = tournament.rounds_list[i].match_list[j][0][1]
            score_two = tournament.rounds_list[i].match_list[j][1][1]
            players_and_scores[player_one] += score_one
            players_and_scores[player_two] += score_two

    players_and_scores = dict(sorted(players_and_scores.items(), key=lambda item: item[1], reverse=True))
    players_and_scores_to_delete = dict(players_and_scores)
    players_list = list(players_and_scores)

    while players_and_scores_to_delete != {}:
        temp_player_list = []
        try:
            temp_player_list.append(players_list[0])
        except IndexError:
            break
        for player in players_list:
            if players_and_scores_to_delete[temp_player_list[0]] == players_and_scores_to_delete[player]:
                if player in temp_player_list:
                    continue
                else:
                    temp_player_list.append(player)

                del players_and_scores_to_delete[player]

        temp_player_list = sorted(temp_player_list, key=lambda player: player.rank, reverse=True)

        for player in temp_player_list:
            players_matchmaking.append(player)
            players_list.remove(player)

    if end is True:
        return players_matchmaking, players_and_scores

    else:
        players_matchmaking = check_if_players_already_played_together(tournament, players_matchmaking)

        prepare_versus_message(players_matchmaking, players_and_scores)

        return players_matchmaking


def check_if_players_already_played_together(tournament, players_matchmaking):
    """Arrange matchmaking player list and return player list according."""
    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_two = tournament.rounds_list[i].match_list[j][1][0]

            if player_one == players_matchmaking[0] and player_two == players_matchmaking[1]:
                roundview.display_players_already_played_together(player_one, player_two)
                players_matchmaking[1], players_matchmaking[2] = (players_matchmaking[2], players_matchmaking[1])

    return players_matchmaking


def prepare_versus_message(players_matchmaking, players_and_scores):
    """Prepare arguments to display versus message."""
    players_matchmaking_for_view = players_matchmaking
    players_and_scores_for_view = players_and_scores
    for i in range(len(players_matchmaking_for_view) // 2):
        roundview.display_other_round_versus(i, players_matchmaking_for_view, players_and_scores_for_view)
        players_matchmaking_for_view = players_matchmaking_for_view[1:]
