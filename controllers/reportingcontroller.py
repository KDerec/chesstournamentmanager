"""Define a reporting."""


from views import reportingview
from views import errorview
from models.database import Database
from models.encoder import encode_json_to_dict


def display_reporting():
    while True:
        try:
            choice = reportingview.choice_report_to_display()
            
            if choice == 1:
                while True:
                    try:
                        choice = reportingview.wich_order()
                        if choice == 1:
                            player_list = sort_players_list_by_alphabetical_order()
                            reportingview.display_players_report(player_list)
                            break
                        elif choice == 2:
                            player_list = sort_players_list_by_rank_order()
                            reportingview.display_players_report(player_list)
                            break
                        elif choice == 3:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 2:
                while True:
                    try:
                        report = reportingview.DisplayTournamentPlayersReport()
                        choice = reportingview.wich_order()
                        if choice == 1:
                            report.by_alphabetical_order()
                        if choice == 2:
                            report.by_rank_order()
                        elif choice == 3:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 3:
                reportingview.display_all_tournament_report()

            elif choice == 4:
                reportingview.display_all_rounds_tournament_report()

            elif choice == 5:
                reportingview.display_all_matchs_tournament_report()

            elif choice == 6:
                break

            else:
                errorview.display_wrong_choice_message()

        except ValueError:
            errorview.display_not_an_integer_message()
                

def sort_players_list_by_alphabetical_order():
    player_list = []
    for player in Database().player_table:
        player = encode_json_to_dict(player)
        player_list.append(player)
    player_list.sort(key= lambda player: player.get('last_name'))

    return player_list


def sort_players_list_by_rank_order():
    player_list = []
    for player in Database().player_table:
        player = encode_json_to_dict(player)
        player_list.append(player)
    player_list.sort(key= lambda player: player.get('rank'))

    return player_list