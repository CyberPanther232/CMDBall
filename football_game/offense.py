import random
from classes import *

# Offense Settings
OVERALL_OFF_PERC = .40

SCREEN_RISK = 50
SHORT_PASS_RISK = 60
DEEP_PASS_RISK = 100
HAIL_MARY_RISK = 150
INSIDE_RUN_RISK = 40
OUTSIDE_RUN_RISK = 50
QB_TOSS_RISK = 55
QB_SNEAK_RISK = 60
FLEA_FLICKER_RISK = 90
FAKE_PASS_RISK = 80

OFFENSE_RISK = .20

# Offensive Play Calls
OPTIONS = {1 : "Passing", 2 : "Running", 3 : "Special"}
PASSING_PLAYS = {1 : "Screen Pass", 2 : "Short Pass", 3 : "Deep Pass", 4 : "Hail Mary"}
RUNNING_PLAYS = {1 : "Inside Run", 2 : "Outside Run", 3 : "QB Toss", 4 : "QB Sneak"}
SPECIAL_PLAYS = {1 : "QB Kneel", 2 : "Flea-Flicker", 3 : "Fake Pass"}

def offensive_probability(user, value) -> float:

    if value == "Screen Pass":
        return float(((int(user.team.offense.passing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * SCREEN_RISK)) / 40)
    
    elif value == "Short Pass":
        return float(((int(user.team.offense.passing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * SHORT_PASS_RISK)) / 40)
    
    elif value == "Deep Pass":
        return float(((int(user.team.offense.passing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * DEEP_PASS_RISK)) / 40)
    
    elif value == "Hail Mary":
        return float(((int(user.team.offense.passing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * HAIL_MARY_RISK)) / 40)
    
    elif value == "Inside Run":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * INSIDE_RUN_RISK)) / 40)
    
    elif value == "Outside Run":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * OUTSIDE_RUN_RISK)) / 40)
    
    elif value == "Inside Run":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * INSIDE_RUN_RISK)) / 40)
    
    elif value == "QB Toss":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * QB_TOSS_RISK)) / 40)
    
    elif value == "QB Sneak":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * QB_SNEAK_RISK)) / 40)
    
    elif value == "QB Kneel":
        return float(((40 / 40)))
    
    elif value == "Flea-Flicker":
        return float(((int(user.team.offense.passing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * FLEA_FLICKER_RISK)) / 40)
    
    elif value == "Fake Pass":
        return float(((int(user.team.offense.rushing) * OVERALL_OFF_PERC) - (OFFENSE_RISK * FAKE_PASS_RISK)) / 40)

def call_offensive_play(user):
    if user.username != "Computer":
        while True:
            print("You are on offense.\nSelect a play below:\n")

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

                
            if choice == "Passing":
                print("You have selected passing plays.\nSelect a play below or press enter to go back:\n")
                for key, value in PASSING_PLAYS.items():
                    print(f"{key}. {value}")
                    print(f"Success Rate: {round(offensive_probability(user, value) * 100, 2)}%\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = PASSING_PLAYS[play]
                        break

                except Exception as e:
                    print(f"Error, invalid playcall... {e}")
            
            elif choice == "Running":
                print("You have selected running plays.\nSelect a play below or press enter to go back:\n")
                for key, value in RUNNING_PLAYS.items():
                    print(f"{key}. {value}")
                    print(f"Success Rate: {round(offensive_probability(user, value) * 100, 2)}%\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = RUNNING_PLAYS[play]
                        break

                except Exception as e:
                    print(f"Error, invalid playcall... {e}")

            elif choice == "Special":
                print("You have selected special plays.\nSelect a play below or press enter to go back:\n")
                for key, value in SPECIAL_PLAYS.items():
                    print(f"{key}. {value}")
                    print(f"Success Rate: {round(offensive_probability(user, value) * 100, 2)}%\n")

                try:
                    play = int(input("Enter option as a number: "))

                    if play < 0 or play > 3:
                        print("Invalid option... Please try again!")
                    else:
                        choice = SPECIAL_PLAYS[play]
                        break

                except Exception as e:
                        print(f"Error, invalid playcall... {e}")

        prob = offensive_probability(user, choice)

        return choice, prob

    else:
        com_choice = random.randint(1, 3)
        com_choice = OPTIONS[com_choice]

        if com_choice == "Passing":
            com_choice = random.randint(1, 4)
            com_choice = PASSING_PLAYS[com_choice]
        elif com_choice == "Running":
            com_choice = random.randint(1, 4)
            com_choice = RUNNING_PLAYS[com_choice]
        elif com_choice == "Special":
            com_choice = random.randint(1, 3)
            com_choice = SPECIAL_PLAYS[com_choice]

            
        prob = offensive_probability(user, com_choice)

        return com_choice, prob

