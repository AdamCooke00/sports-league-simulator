class League():
    def __init__(self, league_name, nrOfTeams):
        self.league_name = league_name
        self.nrOfTeams = nrOfTeams
        self.teams = []
        self.seasons = []

    def __str__(self):
        return "{} - {} teams.".format(self.league_name, self.nrOfTeams)

    def set_teams(self, teams):
        if self.nrOfTeams < len(teams):
            raise Exception("Too many teams for this league")
        self.teams = teams
        print("Here")

    def add_team(self, team):
        self.teams.append(team)

    def add_season(self, season):
        self.seasons.append(season)

    def get_seasons(self):
        return self.seasons

    def get_nrOfTeams(self):
        return self.nrOfTeams
    
    def get_teams(self):
        return self.teams

    def get_league_name(self):
        return self.league_name