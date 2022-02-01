from controllers import menucontroller


def main():

    menucontroller.run()

    # for i in range(tournament.number_of_rounds):
    #     choice = 'O' #input(f'Commencer le tour {i+1} ? Oui = o')
    #     if choice.upper() == 'O':
    #         round = create_round(i)
    #         print(round.name)
    #         player_matchmaking = matchmaking(round, tournament)
    #         choice = 'O' #input(f'Terminer le tour {i+1} ? Oui = o')
    #         if choice.upper() == 'O':
    #             round.ending_date = '{}'.format(time.strftime("%Y-%m-%d_%Hh"))
    #             results = create_match_results(player_matchmaking)
    #             match_list = create_match_list(results, player_matchmaking)
    #             round.match_list = match_list
    #             tournament.add_round_in_rounds_list(round)
    
    # classement, player_matchmaking = matchmaking(round, tournament, end = True)
    # print('\nLes résultats du tournoi sont : ')
    # for i in range(len(classement)):
    #     print(f'{i+1}# avec {classement[player_matchmaking[i]]} points: '
    #     f'{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}')
        
                

if __name__ == "__main__":
    main()