import random

# Team parameters
# Offense high and low
RUSH_HIGH = 99
RUSH_LOW = 60
PASS_HIGH = 99
PASS_LOW = 60

# Defense high and low
ZONE_HIGH = 99
ZONE_LOW = 60
MAN_HIGH = 99
MAN_LOW = 60
BLITZ_HIGH = 99
BLITZ_LOW = 60

# Special Teams high and low
KICKOFF_HIGH = 99
KICKOFF_LOW = 60
PUNT_HIGH = 99
PUNT_LOW = 60
FIELD_GOAL_HIGH = 99
FIELD_GOAL_LOW = 60

# Game settings
GAMES_IN_SEASON = 17
TEAMS_IN_PLAYOFF = 12

def generate_teams() -> None:

    teams = ["CAR", "HOU", "NO", "ATL", "TB",
                "LAR", "LAC", "KC", "LV", "DEN",
                "NYG", "NYJ", "GB", "MIA", "JAX",
                "CIN", "CLE", "ARI", "SF", "DAL",
                "DET", "MIN", "CHI", "NE", "PIT",
                "TEN", "BAL", "WAS", "BUF", "PHI",
                "IND", "SEA"]

    with open('team_data.csv', 'w') as datafile:
        datafile.write('Team_Name,Passing_Rating,Rushing_Rating,Offensive_Rating,Zone_Rating,Man_Rating,Blitz_Rating,Defensive_Rating,Kickoff_Rating,Punt_Rating,Field_Goal_Rating,Special_Teams_Rating,Overall_Rating\n')


        for team in teams:

            rush = random.randint(RUSH_LOW,RUSH_HIGH)
            passing = random.randint(PASS_LOW,PASS_HIGH)
            offesive = (rush + passing) / 2

            zone = random.randint(ZONE_LOW,ZONE_HIGH)
            man = random.randint(MAN_LOW,MAN_HIGH)
            blitz = random.randint(BLITZ_LOW,BLITZ_HIGH)
            defensive = (zone + man + blitz) / 3

            kickoff = random.randint(KICKOFF_LOW, KICKOFF_HIGH)
            punt = random.randint(PUNT_LOW, PUNT_HIGH)
            field_goal = random.randint(FIELD_GOAL_LOW, FIELD_GOAL_HIGH)
            special = (kickoff + punt + field_goal) / 3

            overall = (offesive + defensive + special) / 3

            datafile.write(f'{team},{rush},{passing},{offesive},{zone},{man},{blitz},{defensive},{kickoff},{punt},{field_goal},{special},{overall}\n')
        
        datafile.close()

    print("Teams created! Data saved!")

def name_translation(abbrv) -> str:
    team_names = {"CAR":"Carolina Panthers","HOU":"Houston Texans","NO":"New Orleans Saints","ATL":"Atlanta Falcons","TB":"Tampa Bay Buccanneers",
                "LAR":"Los Angeles Rams","LAC":"Los Angeles Chargers","KC":"Kansas City Chiefs","LV":"Las Vegas Raiders","DEN":"Denver Broncos",
                "NYG":"New York Giants","NYJ":"New York Jets","GB":"Green Bay Packers","MIA":"Miami Dolphins","JAX":"Jacksonville Jaguars",
                "CIN":"Cinninati Bengals","CLE":"Cleveland Browns","ARI":"Arizona Cardinals","SF":"San Francisco 49ers","DAL":"Dallas Cowboys",
                "DET":"Detroit Lions","MIN":"Minnesota Vikings","CHI":"Chicago Bears","NE":"New England Patriots","PIT":"Pittsburgh Steelers",
                "TEN":"Tennessee Titans","BAL":"Baltimore Ravens","WAS":"Washington Commanders","BUF":"Buffalo Bills","PHI":"Philadelphia Eagles",
                "IND":"Indianapolis Colts","SEA":"Seattle Seahawks"}
    
    return team_names[abbrv]

def stadium_translation(abbrv):
    stadiums = {"CAR":"Bank of America Stadium","HOU":"NRG Stadium","NO":"Caesars Superdome","ATL":"Mercedes-Benz Superdome","TB":"Raymond James Stadium",
                "LAR":"SoFi Stadium","LAC":"SoFi Stadium","KC":"Arrowhead Stadium","LV":"Alligiant Stadium","DEN":"Empower Field at MileHigh",
                "NYG":"MetLife Stadium","NYJ":"MetLife Stadium","GB":"Lambeau Field","MIA":"Hard Rock Stadium","JAX":"EverBank Stadium",
                "CIN":"Paycor Stadium","CLE":"Huntington Bank Field","ARI":"State Farm Stadium","SF":"Levi's Stadium","DAL":"AT&T Stadium",
                "DET":"Ford Field","MIN":"U.S. Bank Stadium","CHI":"Soldier Field","NE":"Gillette Stadium","PIT":"Acrisure Stadium",
                "TEN":"Nissan Stadium","BAL":"M&T Bank Stadium","WAS":"Northwest Stadium","BUF":"Highmark Stadium","PHI":"Lincoln Financial Field",
                "IND":"Lucas Oil Stadium","SEA":"Lumen Field"}
    
    return stadiums[abbrv]

def create_schedule(team) -> list:

    divisions = []
    divisions.append(['AFC NORTH', 'BAL', 'PIT', 'CIN', 'CLE'])
    divisions.append(['AFC SOUTH', 'HOU', 'IND', 'TEN', 'JAX'])
    divisions.append(['AFC EAST', 'BUF', 'MIA', 'NE', 'NYJ'])
    divisions.append(['AFC WEST', 'KC', 'LAC', 'DEN', 'LV'])
    divisions.append(['NFC NORTH', 'MIN', 'DET', 'CHI', 'GB'])
    divisions.append(['NFC SOUTH', 'CAR', 'NO', 'ATL', 'TB'])
    divisions.append(['NFC EAST', 'NYG', 'PHI', 'DAL', 'WAS'])
    divisions.append(['NFC WEST', 'SF', 'SEA', 'ARI', 'LAR'])

    for div in divisions:
        if team in div[1:]:
            print(f'Your team is in the {div[0]}!\nYour rivals are below:\n')
            rivals = div[1:]
            selected_division = div
            for rival in rivals:
                if team != rival:
                    print(f"{rival}: {name_translation(rival)}")

    
    print("Selecting teams for your schedule!")

    game_count = GAMES_IN_SEASON
    rivals_dict = {selected_division[1]: 0, selected_division[2] : 0, selected_division[3] : 0, selected_division[4] : 0}

    with open('season_schedule.txt', 'w') as season:
        season.write('Game_Number | Home | Away |\n')
        for game in range(GAMES_IN_SEASON):
            if game_count > 6:
                # Select opponents from different divisions for the first few games to mix things up
                opponent_division = random.choice([div for div in divisions if div != selected_division])
                opponent = random.choice(opponent_division[1:])
            elif game_count <= 6:
                # After a certain number of games, stick to selecting from the same division but not including the team itself
                opponent = random.choice([rival for rival in selected_division[1:] if rival != team])

                while rivals_dict[opponent] >= 2:  # Change the condition based on your requirement
                    opponent = random.choice([rival for rival in selected_division[1:] if rival != team])
                
                rivals_dict[opponent] += 1

            location_selection = random.randint(0, 1)
            if location_selection == 0:
                season.write(f'{game + 1} | {team} | {opponent} |\n')
            else:
                season.write(f'{game + 1} | {opponent} | {team} |\n')

            game_count -= 1

                
    print("Schedule created! Starting season now...")
    pass
