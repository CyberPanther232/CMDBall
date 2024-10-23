class Player:

    def __init__(self, username, team, record):
        self.username = username
        self.team = team
        self.record = record

class Team:

    def __init__(self, name, offense, defense, special_teams):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.special_teams = special_teams
        self.offense_rating = offense.overall
        self.defense_rating = defense.overall
        self.special_teams_rating = special_teams.overall
        self.overall = (int(offense.overall) + int(defense.overall) + int(special_teams.overall)) / 3

class Offense:

    def __init__(self, passing_rating, rushing_rating):
        self.passing = passing_rating
        self.rushing = rushing_rating
        self.overall = (int(passing_rating) + int(rushing_rating)) / 2

class Defense:

    def __init__(self, zone_rating, man_rating, blitz_ranking):
        self.zone = zone_rating
        self.man = man_rating
        self.blitz = blitz_ranking
        self.overall = (int(zone_rating) + int(man_rating) + int(blitz_ranking)) / 3


class Special_Teams:

    def __init__(self, kickoff_rating, punt_rating, field_goal_rating):
        self.kickoff = kickoff_rating
        self.punt = punt_rating
        self.field_goal = field_goal_rating
        self.overall = (int(kickoff_rating) + int(punt_rating) + int(field_goal_rating)) / 3

class Game:

    def __init__(self, home_team, away_team, location, duration):
        self.home_team = home_team
        self.away_team = away_team
        self.location = location
        self.home_score = 0
        self.away_score = 0
        self.duration = duration
        self.quarters = 4

    def home_scored(self, score):

        if score == "touchdown":
            self.home_score += 6

        elif score == "extra point":
            self.home_score += 1
        
        elif score == "field goal":
            self.home_score += 3

        elif score == "safety":
            self.home_score += 2

    def away_scored(self, score):

        if score == "touchdown":
            self.away_score += 6

        elif score == "extra point":
            self.away_score += 1
        
        elif score == "field goal":
            self.away_score += 3

        elif score == "safety":
            self.away_score += 2

    def turn_taken(self):
        self.duration -= 1

        if self.duration == 0:
            print("End of quarter!")
            self.quarters -= 1
            if self.quarters == 2:
                print("Halftime!")

