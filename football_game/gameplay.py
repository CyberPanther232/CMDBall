import random
import time
from game_functions import stadium_translation, name_translation
from kickoff import *
from defense import *
from offense import *
from special_teams import *
from classes import *

# Game settings
TURNS_IN_QUARTER = 14
QUARTERS = 4
DOWNS = {1 : "1st", 2 : "2nd", 3 : "3rd", 4 : "4th"}

# Play Ranges
PLAY_RANGES = {"Short Pass" : (5, 15),"Deep Pass" : (16, 60),"Hail Mary" : (40, 65),
               "Screen Pass" : (0, 5),"Inside Run" : (1, 15),"Outside Run" : (1, 15),
               "Flea-Flicker" : (5, 45), "QB Kneel" : (-2, -2), "Fake Pass" : (1, 15),
               "QB Toss" : (0, 15), "QB Sneak" : (1, 5), "Man-Coverage" : (-1, -10),
               "Zone-Coverage" : (-1, -10), "Blitz" : (-5, -15), "Field Goal Attempt" : (15, 60),
               "Low Punt" : (10, 50), "High Punt" : (15, 60), "Field Goal" : (10, 30), "Two-Point Conversion" : (5, 25),
               "Fake Field Goal" : (5, 15), "Fake Punt" : (5, 15)}

# Risks Percentages
TURNOVER_RISK = .05
MISS_TACKLE_RISK = .05
OFFENSIVE_RANDOM = .1
DEFENSIVE_RANDOM = .1

def random_factors(player, computer, possession):
    if possession == computer.team.name:
        
        off_random_factor = (computer.team.offense.overall * OFFENSIVE_RANDOM) - (computer.team.offense.overall * TURNOVER_RISK)
        def_random_factor = (player.team.defense.overall * DEFENSIVE_RANDOM) - (player.team.offense.overall * MISS_TACKLE_RISK)

    else:
        off_random_factor = (player.team.offense.overall * OFFENSIVE_RANDOM) - (player.team.offense.overall * TURNOVER_RISK)
        def_random_factor = (computer.team.defense.overall * DEFENSIVE_RANDOM) - (computer.team.offense.overall * MISS_TACKLE_RISK)

    if off_random_factor > def_random_factor:
        extra = random.choice(range(1, 10))
        print(f"The {possession} gained an extra {extra} yard(s) due to mistackling by the defense!")
        return possession, extra, False
    
    else:

        turnover_num = random.random()
        if turnover_num < TURNOVER_RISK:
            print("The ball has been turned over by the offense!")
            if possession == computer.team.name:
                possession = player.team.name
                return possession, 0, True
            else:
                possession = computer.team.name
                return possession, 0, True

        else:
            extra = random.choice(range(-1,-10, -1))
            print(f"The defense pushed the offense back {abs(extra)} yards!")
            return possession, extra, False

def evaluate_play_success(probability):

    random_number = random.random()

    if random_number < probability:
        return True
    else:
        return False

# Type is the type of play called by the user, Com_Type is the type of play called by the Computer
def run_play(type, probability, com_type, com_probability, computer, possession, count):

    if DOWNS[count] == "4th" and possession == computer.team.name:
        kicking = com_type
        receiving = type
    
    elif DOWNS[count] == "4th":
        kicking = type
        receiving = com_type


    if possession == computer.team.name:
        offense = com_type
        defense = type

        # Determine success of play
        offense_success = evaluate_play_success(com_probability)
        defense_success = evaluate_play_success(probability)

    else:
        offense = type
        defense = com_type

        # Determine success of play
        offense_success = evaluate_play_success(probability)
        defense_success = evaluate_play_success(com_probability)
    
    if offense_success:
        yardage = max(PLAY_RANGES[offense])

    else:
        yardage = min(PLAY_RANGES[offense])

    if defense_success:
        loss = max(PLAY_RANGES[defense])
    
    else:
        loss = min(PLAY_RANGES[defense])

    return yardage - loss

def run_game(game_number, player) -> str:
    with open('season_schedule.txt', 'r') as season:
        for line in season.readlines():
            fields = line.strip().split(' |')
            if game_number == fields[0]:
                home = fields[1].strip(' ')
                away = fields[2].strip(' ')
                print(f"It is gametime at {stadium_translation(home)} as the {name_translation(away)} play the {name_translation(home)} at home!")
    season.close()

    game = Game(home, away, stadium_translation(home), TURNS_IN_QUARTER)

    if home == player.team.name:
        HOME = True
    else:
        HOME = False

    with open('team_data.csv', 'r') as teams:
        for line in teams.readlines():
            fields = line.strip().split(',')
            if fields[0] == away and HOME:         
                com = Player("Computer", Team(away, Offense(fields[1], fields[2]), Defense(fields[4], fields[5], fields[6]), Special_Teams(fields[8], fields[9], fields[10])), '0 -- 0')
            elif fields[0] == home and not HOME:              
                com = Player("Computer", Team(home, Offense(fields[1], fields[2]), Defense(fields[4], fields[5], fields[6]), Special_Teams(fields[8], fields[9], fields[10])), '0 -- 0')
    teams.close()

    coin = random.choice(['Heads', 'Tails'])
    WIN_COIN = False

    if HOME:
        com_selection = random.choice(['Heads', 'Tails'])
        print(f"Since {name_translation(com.team.name)} are the guests they will pick a side for the coin toss...")
        print(f"The {com.team.name} selected {com_selection}!")

        if coin == com_selection:
            print("Your opponent has won the coin toss...")
            com_selection = random.choice(['Kick', 'Receive'])
            print(f"Your opponent has selected to {com_selection} the ball")
        else:
            print("You have won the coin toss!")
            WIN = True

    else:
        print(f"Since you are the guest you get to select a side for the coin toss!")
        while True:
            try:
                user_selection = int(input("Enter a number (1 for Heads, 0 for Tails): "))
                if user_selection < 0 or user_selection > 1:
                    print("Invalid input... Please enter a 1 for Heads or 0 for Tails")
                else:
                    if user_selection == 0:
                        user_selection = "Tails"
                    else:
                        user_selection = "Heads"
                    break
            except Exception as e:
                print("Error... Invalid input... Try again!")

    
        if user_selection == coin:
            print("You have won the coin toss!")
            com_selection = ""
            WIN_COIN = True
        else:
            print("Your opponent has won the coin toss...")
            com_selection = random.choice(['Kick', 'Receive'])
            print(f"Your opponent has selected to {com_selection} the ball")
    
    if WIN_COIN:
        while True:
            try:
                user_selection = int(input("Enter a number (1 for Kick, 0 for Receive): "))
                if user_selection < 0 or user_selection > 1:
                    print("Invalid input... Please enter a 1 for Kick or 0 for Receive")
                else:
                    if user_selection == 0:
                        user_selection = "Receive"
                    else:
                        user_selection = "Kick"
                break
            except Exception as e:
                print("Error... Invalid input... Try again!")
    
    if WIN_COIN and user_selection == "Receive":
        possession, distance = kickoff(player, com, com.username)
    elif WIN_COIN and user_selection == "Kick":
        possession, distance = kickoff(player, com, player.username)
    else:
        if com_selection == "Receive":
            possession, distance = kickoff(player, com, player.username)
        else:
            possession, distance = kickoff(player, com, com.username)

    return_distance = kickoff_return(player, com, possession)

    # Sets territory and yardline
    yardline = 50 - int(distance) + return_distance
    territory = "own"

    # Display kick distance
    print(f"Kick Distance: {distance} | Return Distance: {return_distance} | Yardline: {yardline}")

    # Test for touchback
    if int(distance) - 50 > 0 and yardline < 100:
        print(f"Touchback! The {name_translation(possession)} will start it at the 30 yard line!")
        yardline = 30

    else:

        if yardline >= 100:
            if possession == home:
                game.home_scored("touchdown")
                print(f"The kick has been returned for a touchdown! The {name_translation(possession)} put six on the board!")
                print(f'Current Score:\nHOME:{game.home_score} | AWAY: {game.away_score}')
                pass
            else:
                game.away_scored("touchdown")
                print(f"The kick has been returned for a touchdown! The {name_translation(possession)} put six on the board!")
                print(f'Current Score:\nHOME:{game.home_score} | AWAY: {game.away_score}')
                pass

        elif yardline > 50:
            difference = yardline - 50
            yardline = yardline - difference
            territory = "opposing"

        print(f"Kickoff returned for {return_distance} yards! {possession} will start it at the {yardline} in their {territory} territory!")

    count = 1
    yards_to_gain = 10
    
    # While loop to manage game and turn systems
    while True:
        for quarter in range(0, QUARTERS):
            if quarter == 3:
                print("Halftime!")
            
            for turn in range(0, TURNS_IN_QUARTER):
                print(f"The {name_translation(possession)} have the ball at the {yardline} yardline!")
                
                if com.team.name == possession and DOWNS[count] != "4th":
                    com_play, com_probability = call_offensive_play(com)
                    play, probability = call_defensive_play(player)
                    count += 1
                
                elif player.team.name == possession and DOWNS[count] != "4th":
                    play, probability = call_offensive_play(player)
                    com_play, com_probability = call_defensive_play(com)
                    count += 1

                elif com.team.name == possession and DOWNS[count] == "4th":
                    com_play, com_probability = call_special_play(com)
                    play = ""
                    probability = 0
                    count = 1
                
                elif player.team.name == possession and DOWNS[count] == "4th":
                    play, probability = call_special_play(player)
                    com_play = 0
                    com_probability = 0
                    count = 1

                yards = run_play(play, probability, com_play, com_probability, com, possession)
                possession, extra, turnover = random_factors(player, com, possession)
                
                print(possession, extra)

                if territory == "own" and yardline < 50:
                    yardline = yardline - (yards + extra if extra > 0 else -extra)
                    yards_to_gain = yards_to_gain + (yards + extra)

                elif territory == "opposing":
                    yardline = yardline + (yards + extra if extra > 0 else -extra)

                if turnover:
                    print(f"The {possession} take over from the {yardline} yardline!")
                    count = 1

                if yardline <= 0:
                    print(f"Touchdown {possession}!")
                    if possession == home:
                        game.home_scored("touchdown")
                    else:
                        game.away_scored("touchdown")

                    print(f"The Score is now: HOME: {game.home_score} | AWAY: {game.away_score}")
                    print(f"The {possession} will now try for the extra point!")

                    ### Insert extra point function here

                if yards_to_gain < 0:
                    print(f"And with that play the {possession} have another first down at the {yardline} yardline!")
                    yards_to_gain = 10
                    count = 1

                if yards_to_gain > 0 and DOWNS[count] == "4th":
                    print(f"The {possession} will now have to make a decision on fourth down!")

                

run_game("1", Player('test', Team('GGG', Offense(90, 90), Defense(90, 90, 90), Special_Teams(90, 90, 90)), '0 -- 0'))