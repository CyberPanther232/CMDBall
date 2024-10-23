import random


KICK_RISK = .20
SPECIAL_TEAMS_PERC = 1
OPP_SPECIAL_TEAMS_PERC = .20
KICK_RETURN_PERC = .10
HIGH_KICK_RANGE = (40, 60)
SHORT_KICK_RANGE = (20, 40)
ONSIDE_KICK_RANGE = (5, 10)

# Special Teams Plays
special_teams_plays_kickoff = {1 : "High Kick", 2 : "Short Kick", 3 : "Onside Kick"}

def kickoff_probability(kicker, opponent, play) -> float:

    if play == "High Kick":
        risk_level = 30
    elif play == "Short Kick":
        risk_level = 80
    else:
        risk_level = 180

    probability = 0

    probability = ((kicker.team.special_teams.overall * SPECIAL_TEAMS_PERC) - (opponent.team.special_teams.overall * OPP_SPECIAL_TEAMS_PERC) - (KICK_RISK * risk_level)) / 100

    return probability

def kickoff_return(user, computer, possession):

    random_number = random.random()

    user_stat = int(user.team.special_teams.kickoff)
    com_stat = int(computer.team.special_teams.kickoff)

    if possession == "Computer":

        if random_number < KICK_RETURN_PERC:
            return 100
        else:
            pass

        return round(com_stat * KICK_RETURN_PERC, 0)
    else:
        if random_number < KICK_RETURN_PERC:
            return 100
        else:
            pass
        return round(user_stat * KICK_RETURN_PERC, 0)

def run_kickoff(user, computer, kicking_team, play):

    distance = 0
    user_stat = int(user.team.special_teams.kickoff)
    com_stat = int(computer.team.special_teams.kickoff)
    
    if kicking_team != "Computer":

        probability = kickoff_probability(user, computer, play)

        print(f"{user.username} kicks the ball of with a {play}!")

        random_number = random.random()

        if random_number <= probability and play == "High Kick":
            
            distance = (user_stat / 100) * max(HIGH_KICK_RANGE)
        
        elif random_number > probability and play == "High Kick":

            distance = (user_stat / 100) * min(HIGH_KICK_RANGE)

        elif random_number <= probability and play == "Short Kick":

            distance = (user_stat / 100) * max(SHORT_KICK_RANGE)

        elif random_number > probability and play == "Short Kick":

            distance = (user_stat / 100) * min(SHORT_KICK_RANGE)

        elif random_number <= probability and play == "Onside Kick":

            distance = (user_stat / 100) * max(ONSIDE_KICK_RANGE)
            print(f"The onside kick attempt was successful! {kicking_team} retains possession of the football!")
            return user.team.name, round(distance, 0)
        
        elif random_number > probability and play == "Onside Kick":
            
            distance = (user_stat / 100) * min(ONSIDE_KICK_RANGE)
            print("The onside kick attempt failed...")

        return computer.team.name, round(distance, 0)
    
    else:
        print(f"{computer.username} kicks the ball of with a {play}!")
        
        probability = kickoff_probability(computer, user, play)

        random_number = random.random()

        if random_number <= probability and play == "High Kick":
            
            distance = (com_stat / 100) * max(HIGH_KICK_RANGE)
        
        elif random_number > probability and play == "High Kick":

            distance = (com_stat / 100) * min(HIGH_KICK_RANGE)

        elif random_number <= probability and play == "Short Kick":

            distance = (com_stat / 100) * max(SHORT_KICK_RANGE)

        elif random_number > probability and play == "Short Kick":

            distance = (com_stat / 100) * min(SHORT_KICK_RANGE)

        elif random_number <= probability and play == "Onside Kick":

            distance = (com_stat / 100) * max(ONSIDE_KICK_RANGE)
            print(f"The onside kick attempt was successful!{kicking_team} Retains possession of the football!")
            return user.team.name, round(distance, 0)
        
        elif random_number > probability and play == "Onside Kick":
            
            distance = (com_stat / 100) * min(ONSIDE_KICK_RANGE)
            print("The onside kick attempt failed...")

        return user.team.name, round(distance, 0)

def kickoff(user, computer, kicking_team):

    if kicking_team != "Computer":
        while True:
            print("You are kicking the ball.\nSelect a play below:\n")
            for key, value in special_teams_plays_kickoff.items():
                print(f"{key}. {value}")
                print(f"Success Rate: {round(kickoff_probability(user, computer, value) * 100, 2)}%\n")
            
            try:
                play = int(input("Enter option as a number: "))

                if play < 0 or play > 3:
                    print("Invalid option... Please try again!")
                else:
                    choice = special_teams_plays_kickoff[play]
                    distance, possession = run_kickoff(user, computer, kicking_team, choice)
                    break

            except Exception as e:
                print(f"Error, invalid playcall... {e}")

    else:
        com_choice = random.randint(1, 2)
        com_choice = special_teams_plays_kickoff[com_choice]
        distance, possession = run_kickoff(user, computer, kicking_team, com_choice)

    return distance, possession