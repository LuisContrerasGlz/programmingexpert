"""

For this project you will be asked to create a program that can schedule games that teams will play in an end of year tournament. You will only be responsible for determining the games played in the first round of the tournament.

You will first need to ask the user of your program to input the number of teams; you may assume there will always be an even number of teams (you don't need to validate this). Next you will need to ask for the names of all of the teams and store them in some way.

After this you'll need to determine the number of games that were played by each team; you may assume each team plays the same number of games. Finally, you'll need to determine the number of wins each team had during the regular season.

When asking for user input, you'll need to make sure all input is valid and ask the user to try again if they give you invalid input. You may assume user input will always be the correct type (i.e. if you ask for a number you will always get an integer). You can determine if the input is invalid by looking at the following constraints:

There are always at least 2 teams in the tournament.
Each team plays every other team at least once in the regular season.
All team names contain at most 2 words and at least 2 characters.
Each team has at minimum 0 wins and no more wins than the number of games they played.
In the first round of the tournament the teams with the most regular season wins play the teams with the least regular season wins. For example, if Team A has 5 wins, Team B has 4 wins, Team C has 3 wins and Team D has 2 wins then Team A and Team D play each other and Team B and C play each other. If teams are tied for wins and/or losses then your program can choose any appropriate team.

Your program should output the games that should be played in the format seen below. The first game outputted should contain the team with the most regular season wins, the second game should contain the team with the second most regular season wins, etc. The home team of each game should be the team with the least wins of the two, if there is a tie in wins your program can chose any appropriate team.

"""

import itertools

# Function to validate team name


def is_valid_team_name(name):
    words = name.split()
    return len(words) <= 2 and all(len(word) >= 2 for word in words)

# Function to validate number of games


def is_valid_num_games(num_games, num_teams):
    return num_games >= num_teams - 1

# Function to validate number of wins


def is_valid_num_wins(num_wins, num_games):
    return 0 <= num_wins <= num_games


# Ask for number of teams
while True:
    num_teams = int(input("Enter the number of teams in the tournament: "))
    if num_teams >= 2:
        break
    else:
        print("The minimum number of teams is 2, try again.")

# Ask for team names
teams = []
for i in range(1, num_teams + 1):
    while True:
        name = input("Enter the name for team #{}: ".format(i))
        if is_valid_team_name(name):
            teams.append(name)
            break
        else:
            print(
                "Team names must have at least 2 characters and at most 2 words, try again.")

# Ask for number of games
while True:
    num_games = int(input("Enter the number of games played by each team: "))
    if is_valid_num_games(num_games, num_teams):
        break
    else:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

# Ask for number of wins
wins = []
for team in teams:
    while True:
        num_wins = int(input("Enter the number of wins {} had: ".format(team)))
        if is_valid_num_wins(num_wins, num_games):
            wins.append(num_wins)
            break
        else:
            print(
                "The number of wins must be between 0 and the number of games played, try again.")

# Generate the games
sorted_teams = [team for _, team in sorted(zip(wins, teams), reverse=True)]
games = list(itertools.zip_longest(
    sorted_teams[:num_teams//2], sorted_teams[num_teams//2:]))

# Print the games
print("Generating the games to be played in the first round of the tournament...")
for i, game in enumerate(games):
    home_team, away_team = sorted(game, key=lambda x: wins[teams.index(x)])
    print("Game #{}: Home: {} VS Away: {}".format(i+1, home_team, away_team))
