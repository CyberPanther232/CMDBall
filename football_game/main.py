"""
Program: CMDBall
Date-Created: 18-Oct-2024
Date-Modifed: 20-Oct-2024
Purpose: This program will act as a fun offline command prompt based football game that will involve real-time decision-making and play-calling.
"""
import time
from classes import *
from game_functions import *

def main():
    print("Welcome to CMDBALL! This is the text-based command line football game! Test your ability to lead, call plays, and win games!")

    time.sleep(2)

    username = str(input("Enter username: "))
    print(f"Let's begin {username}!")

    print("Randomly generating teams w/stats...")
    generate_teams()

    team_count = 0
    selected_team = ""

    print("Now time to select your team!")
    while selected_team == "":
        with open('team_data.csv', 'r') as teams:
            for team in teams.readlines():
                fields = team.strip().split(',')
                print(fields)
                team_count += 1
                if team_count == 5:
                    team_count = 0
                    selected_team = input("Type team name for press enter to see other teams: ").upper()
                    if selected_team == "":
                        pass
                    else:
                        print(f"You've selected the {name_translation(selected_team)}!")
                        offense_stats = Offense(fields[1],fields[2])
                        defense_stats = Defense(fields[4],fields[5],fields[6])
                        special_stats = Special_Teams(fields[8],fields[9],fields[10])

                        team_stats = Team(selected_team, offense_stats, defense_stats, special_stats)
                        player = Player(username, team_stats, "0 -- 0")
                        break

                    print('Team_Name, Passing_Rating, Rushing_Rating, Offensive_Rating, Zone_Rating, Man_Rating, Defensive_Rating, Kickoff_Rating, Punt_Rating, Field_Goal_Rating, Special_Teams_Rating, Overall_Rating')

    create_schedule(selected_team)


    
    


if __name__ == "__main__":
    main()