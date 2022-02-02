from controllers import menucontroller


def main():

    menucontroller.run()
   
    # classement, player_matchmaking = matchmaking(round, tournament, end = True)
    # print('\nLes résultats du tournoi sont : ')
    # for i in range(len(classement)):
    #     print(f'{i+1}# avec {classement[player_matchmaking[i]]} points: '
    #     f'{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}')
        
                

if __name__ == "__main__":
    main()