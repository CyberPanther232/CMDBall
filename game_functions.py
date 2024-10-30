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

    teams = ["BRB", "DH", "ICP", "NW", "SS",
             "GGG", "PR", "MT", "EE", "SCT",
             "CCD", "GB", "CCU", "RCR", "FBF",
             "VVI", "CCH", "WW", "MM", "HH",
             "NN", "SST", "VV", "PP", "TVT",
             "FF", "SRS", "TT", "CCY"]

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
    team_names = {
        "BRB": "Blue Ridge Brawlers", "DH": "Desert Hawks", "ICP": "Ironclad Pirates",
        "NW": "Northern Wolves", "SS": "Savannah Storm", "GGG": "Golden Gate Guardians",
        "PR": "Pacific Raiders", "MT": "Midwest Thunderbirds", "EE": "Eastern Eagles",
        "SCT": "Steel City Titans", "CCD": "Capitol Crusaders", "GB": "Glacier Bears",
        "CCU": "Canyon Cougars", "FBF": "Fireball Falcons", "VVI": "Valley Vipers",
        "CCH": "Coastal Crushers", "RCR": "River City Rattlers", "WW": "Wilderness Wolves",
        "MM": "Mountain Men", "HH": "Horizon Hornets", "NN": "Nomad Navigators",
        "SST": "Starlight Stallions", "VV": "Vortex Vultures", "PP": "Phantom Phantoms",
        "TVT": "Thunder Valley Titans", "FF": "Fusion Flames", "SRS": "Steel River Sentries",
        "TT": "Titanium Tridents", "CCY": "Crimson Cyclones", "SSV": "Solar Savages", "TWT": "Twilight Tigers",
        "SSH" : "Savage Sharks"
    }

    return team_names[abbrv]

def stadium_translation(abbrv):
    stadiums = {
        "BRB": "Mountain View Arena", "DH": "Sunstone Stadium", "ICP": "Blacksmith Field",
        "NW": "Frostbite Dome", "SS": "Thunderwave Stadium", "GGG": "Bayfront Coliseum",
        "PR": "Oceanview Park", "MT": "Heartland Arena", "EE": "Skyhigh Stadium",
        "SCT": "Ironworks Stadium", "CCD": "Liberty Field", "GB": "Iceberg Arena",
        "CCU": "Rockslide Stadium", "FBF": "Ember Field", "VVI": "Serpent's Nest",
        "CCH": "Shoreline Stadium", "RCR": "Wetlands Park", "WW": "Timberline Stadium",
        "MM": "Summit Arena", "HH": "Skyview Stadium", "NN": "Voyager Field",
        "SST": "Celestial Arena", "VV": "Vulture Stadium", "PP": "Spectral Field",
        "TVT": "Stormwatch Stadium", "FF": "Inferno Arena", "SRS": "Fortress Field",
        "TT": "Ocean Depths Stadium", "CCY": "Cyclone Field", "SSV" : "Radiance Stadium",
        "TWT": "Dusk Dome", "SSH" : "Deep Blue Arena"
    }

    return stadiums[abbrv]


def create_schedule(team) -> list:

    divisions = []
    divisions.append(['PAC NORTH', 'DH', 'ICP', 'NW', 'SS'])
    divisions.append(['PAC SOUTH', 'GGG', 'PR', 'MT', 'EE'])
    divisions.append(['PAC EAST', 'SCT', 'CCD', 'GB', 'CCU'])
    divisions.append(['PAC WEST', 'FBF', 'VVI', 'CCH', 'RCR'])
    divisions.append(['ATL NORTH', 'WW', 'MM', 'HH', 'NN'])
    divisions.append(['ATL SOUTH', 'SST', 'VV', 'PP', 'TVT'])
    divisions.append(['ATL EAST', 'FF', 'SRS', 'TT', 'CCY'])
    divisions.append(['ATL WEST', 'BRB', 'TWT', 'SSV', 'SSH'])

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
