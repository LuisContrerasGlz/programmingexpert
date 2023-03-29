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
