import random
from classes import *

# Defense Settings
OVERALL_DEF_PERC = .40
DEFENSIVE_RISK = .10
MAN_RISK_LEVEL = 60
ZONE_RISK_LEVEL = 40
BLITZ_RISK_LEVEL = 100

# Defensive Plays
DEFENSIVE_PLAYS = {1 : "Man-Coverage", 2 : "Zone-Coverage", 3 : "Blitz"}

def defensive_probability(user, value) -> float:

    if value == "Man-Coverage":
        return float(((int(user.team.defense.man) * OVERALL_DEF_PERC) - (MAN_RISK_LEVEL * DEFENSIVE_RISK)) / 40)
    
    elif value == "Zone-Coverage":
        return float(((int(user.team.defense.zone) * OVERALL_DEF_PERC) - (ZONE_RISK_LEVEL * DEFENSIVE_RISK)) / 40)
    
    elif value == "Blitz":
        return float(((int(user.team.defense.blitz) * OVERALL_DEF_PERC) - (BLITZ_RISK_LEVEL * DEFENSIVE_RISK)) / 40)


def call_defensive_play(user):
    if user.username != "Computer":
        while True:
            print("You are on defense.\nSelect a play below:\n")
            for key, value in DEFENSIVE_PLAYS.items():
                print(f"{key}. {value}")
                print(f"Success Rate: {round(defensive_probability(user, value) * 100, 2)}%\n")
            
            try:
                play = int(input("Enter option as a number: "))

                if play < 0 or play > 3:
                    print("Invalid option... Please try again!")
                else:
                    choice = DEFENSIVE_PLAYS[play]
                    break

            except Exception as e:
                print(f"Error, invalid playcall... {e}")
        
        prob = defensive_probability(user, choice)
        
        return choice, prob

    else:
        com_choice = random.randint(1, 3)
        com_choice = DEFENSIVE_PLAYS[com_choice]
        prob = defensive_probability(user, com_choice)

        return com_choice, prob