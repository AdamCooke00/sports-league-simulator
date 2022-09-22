def display_standings(teams):
    standings = sorted(teams, key=lambda x: x.wins, reverse=True)
    for team in standings:
        wins, losses = team.get_record()
        print(team.team_name() + ": {}-{}".format(wins, losses))

class Division:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

class Conference:
    def __init__(self, name, divisions):
        self.name = name
        self.divisions = divisions
        for division in divisions:
            for team in division:
                self.teams.append(team)

class League():
    def __init__(self, league_name, seasons=[]):
        self.league_name = league_name
        self.seasons = seasons

    def __str__(self):
        return self.league_name