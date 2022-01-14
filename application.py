from constants import TEAMS, PLAYERS
from string import ascii_uppercase


cleaned_players = []
balanced_teams = {}


def print_stats(team, num_players_team):
    experience = 0
    avg_height = 0
    # sorted_team line adapted from https://stackoverflow.com/questions/575819/sorting-dictionary-keys-in-python
    sorted_team = sorted(balanced_teams[team], key = lambda i: i['height'])
    players = []
    guardians = []

    for player in sorted_team:
        if player['experience'] == True:
            experience +=1
        avg_height += player['height']
        players.append(player['name'])
        for guard in player['guardians']:
            guardians.append(guard)
    avg_height /= num_players_team

    print()
    print(f'Team: {team} Stats')
    print('--------------------')
    print(f'Total players: {num_players_team}')
    print(f'Total experienced: {experience}')
    print(f'Total inexperienced: {int(num_players_team - experience)}')
    print(f'Average height: {round(avg_height, 2)}\n')
    print('Players on team:')
    print('----------------')
    for num in range(len(players)):
        print(players[num], end='')
        if num != len(players) - 1:
            print(', ', end='')
    print()
    print()
    print('Guardians:')
    print('----------')
    for num in range(len(guardians)):
        print(guardians[num].strip(), end='')
        if num != len(guardians):
            print(', ', end='')
    print()
    print()


def clean_data(**player):
    new_player = {}
    new_player['name'] = player['player']['name']
    guardian = player['player']['guardians'].split('and')
    new_player['guardians'] = guardian

    if player['player']['experience'] == 'YES':
        new_player['experience'] = True
    elif player['player']['experience'] == 'NO':
        new_player['experience'] = False

    height = player['player']['height'].split()
    new_player['height'] = int(height[0])
    cleaned_players.append(new_player)


def balance_teams(num_players_team):
    num_experienced = 0
    avg_height = 0

    for team in TEAMS:
        balanced_teams[team] = []

    for player in cleaned_players:
        if player['experience'] == True:
            num_experienced += 1
    experience_per_team = num_experienced / len(TEAMS)

    
    for team in balanced_teams:
        num_experienced = 0
        for player in cleaned_players.copy():
            if player['experience'] == True:
                if num_experienced < experience_per_team:
                    balanced_teams[team].append(player)
                    cleaned_players.remove(player)
                    num_experienced +=1

    for team in balanced_teams:
        for player in cleaned_players.copy():
            if len(balanced_teams[team]) < num_players_team:
                    balanced_teams[team].append(player)
                    cleaned_players.remove(player)
      

    

def main():
    num_players_team = len(PLAYERS) / len(TEAMS)
    for player in PLAYERS:
        clean_data(player=player)
    balance_teams(num_players_team)

    print('###### BASKETBALL STATS TOOL ######')
    print()
    while True:
        print('What would you like to do?')
        print()
        print('A) Display Team Stats.')
        print('B) Quit.\n')
        menu_option = input('Choose an option: ')

        if menu_option.upper() == 'A':
            print()
            for i, team in enumerate(balanced_teams):
                print(f'{ascii_uppercase[i]}) {team}')
            print()
            menu_option = input('Choose a team: ')
            if menu_option.upper() == 'A':
                print_stats(TEAMS[0], num_players_team)   
            elif menu_option.upper() == 'B':
                print_stats(TEAMS[1], num_players_team) 
            elif menu_option.upper() == 'C':
                print_stats(TEAMS[2], num_players_team) 
            else:
                print('##Invalid input##\n')

        elif menu_option.upper() == 'B':
            break
        else:
            print('##Invalid Input##\n')



if __name__ == "__main__":
    main()
