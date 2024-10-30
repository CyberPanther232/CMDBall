import random
from classes import *

# Special teams Settings
OVERALL_SPEC_PERC = .40
SPECIAL_RISK = .10
FAKE_FG_LEVEL = 100
TWO_CONV_LEVEL = 115
HIGH_PUNT_LEVEL = 50
LOW_PUNT_LEVEL = 80
FAKE_PUNT_LEVEL = 100
FIELD_GOAL_LEVEL = 30
EXTRA_POINT_LEVEL = 20

# Special Teams Plays
OPTIONS = {1 : "Punt", 2: "Field Goal"}
PUNT_PLAYS = {1 : "High Punt", 2 : "Low Punt", 3 : "Fake Punt"}
FIELD_GOAL_PLAYS = {1 : "Field Goal Attempt", 2: "Fake Field Goal"}
EXTRA_POINT_PLAYS = {1 : "Field Goal", 2 : "Two-Point Conversion"}

def special_teams_probability(user, value) -> float:
    
    if value == "High Punt":
        return float(((int(user.team.special_teams.punt) * OVERALL_SPEC_PERC) - (HIGH_PUNT_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Low Punt":
        return float(((int(user.team.special_teams.punt) * OVERALL_SPEC_PERC) - (LOW_PUNT_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Fake Punt":
        return float(((int(user.team.special_teams.overall) * OVERALL_SPEC_PERC) - (FAKE_PUNT_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Field Goal Attempt":
        return float(((int(user.team.special_teams.field_goal) * OVERALL_SPEC_PERC) - (FIELD_GOAL_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Fake Field Goal":
        return float(((int(user.team.special_teams.overall) * OVERALL_SPEC_PERC) - (FAKE_FG_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Field Goal":
        return float(((int(user.team.special_teams.field_goal) * OVERALL_SPEC_PERC) - (EXTRA_POINT_LEVEL * SPECIAL_RISK) / 40))
    elif value == "Two-Point Conversion":
        return float(((int(user.team.offense.overall) * OVERALL_SPEC_PERC) - (TWO_CONV_LEVEL * SPECIAL_RISK) / 40))


def call_special_play(user, touchdown=False):
    if user.username != "Computer":
        while True:

            if touchdown:
                print(f"Now {user.username} will go for an extra point")
                for key, value in EXTRA_POINT_PLAYS.items():
                    print(f"{key}. {value}\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = EXTRA_POINT_PLAYS[play]
                        

                except Exception as e:
                    print(f"Error, invalid playcall... {e}")

                prob = special_teams_probability(user, choice)

                return choice, prob

            print("You are at fourth down.\nSelect a special teams play below:\n")

            for key, value in OPTIONS.items():
                print(f"{key}. {value}\n")

            try:
                play = int(input("Enter option as a number: "))

                if play < 0 or play > 3:
                    print("Invalid option... Please try again!")
                else:
                    choice = OPTIONS[play]
                    

            except Exception as e:
                print(f"Error, invalid playcall... {e}")

                
            if choice == "Punt":
                print("You have selected passing plays.\nSelect a play below or press enter to go back:\n")
                for key, value in OPTIONS.items():
                    print(f"{key}. {value}")
                    print(f"Success Rate: {round(special_teams_probability(user, value) * 100, 2)}%\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = PUNT_PLAYS[play]
                        break

                except Exception as e:
                    print(f"Error, invalid playcall... {e}")
            
            elif choice == "Field Goal":
                print("You have selected running plays.\nSelect a play below or press enter to go back:\n")
                for key, value in FIELD_GOAL_PLAYS.items():
                    print(f"{key}. {value}")
                    print(f"Success Rate: {round(special_teams_probability(user, value) * 100, 2)}%\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = FIELD_GOAL_PLAYS[play]
                        break

                except Exception as e:
                    print(f"Error, invalid playcall... {e}")


        prob = special_teams_probability(user, choice)

        return choice, prob

    else:

        if touchdown:
            com_choice = random.randint(1, 2)
            com_choice = EXTRA_POINT_PLAYS[com_choice]

        else:
            com_choice = random.randint(1, 3)
            com_choice = OPTIONS[com_choice]

            if com_choice == "Punt":
                com_choice = random.randint(1, 3)
                com_choice = PUNT_PLAYS[com_choice]
            elif com_choice == "Field Goal":
                com_choice = random.randint(1, 2)
                com_choice = FIELD_GOAL_PLAYS[com_choice]
            
        prob = special_teams_probability(user, com_choice)

        return com_choice, prob