import random
from game import Game
from team import Team

class Season():
    def __init__(self, year, games_per_team):
        self.year = year
        self.completed = False
        self.regular_season_completed = False
        self.playoffs_completed = False
        self.games_per_team = games_per_team
        self.champion = None
        self.teams = []
        self.schedule = []
        self.playoff_schedule = []
        self.conferences = []
        self.divisions = []

    def __repr__(self):
        if self.champion:
            return "Season {}\nChampion: {}".format(self.year, self.champion)
        else:
            return "Season {} : {} Games per team.".format(self.year, self.games_per_team)

    def generate_schedule(self):
        games = []
        if len(self.teams) % 2 or len(self.teams) < 1:
            raise Exception("Sorry, cannot make a schedule with odd number of teams.")
        for y in range(self.games_per_team):
            random.shuffle(self.teams)
            for x in range(len(self.teams)//2):
                genGame = Game(self.teams[x*2], self.teams[x*2+1])
                games.append(genGame)
                self.teams[x*2].schedule.append(genGame)
                self.teams[x*2+1].schedule.append(genGame)
        print("Schedule have been generated")
        self.schedule = games

    def simulate(self):
        if self.completed:
            raise Exception("Sorry, season is over")
        if len(self.schedule) < 1:
            raise Exception("Sorry, no games to simulate")
        for game in self.schedule:
            game.simulate()
        print("Season has been simulated")

    def generate_teams(self, nrOfTeams):
        nfl_list = ["Arizona Cardinals","Atlanta Falcons","Baltimore Ravens","Buffalo Bills","Carolina Panthers","Chicago Bears","Cincinnati Bengals","Cleveland Browns","Dallas Cowboys","Denver Broncos","Detroit Lions","GreenBay Packers","Houston Texans","Indianapolis Colts","Jacksonville Jaguars","KansasCity Chiefs","LasVegas Raiders","LosAngeles Chargers","LosAngeles Rams","Miami Dolphins","Minnesota Vikings","NewEngland Patriots","NewOrleans Saints","NewYork Giants","NewYork Jets","Philadelphia Eagles","Pittsburgh Steelers","SanFrancisco 49ers","Seattle Seahawks","TampaBay Buccaneers","Tennessee Titans","Washington Commanders"]
        if nrOfTeams > len(nfl_list):
            raise Exception("Too many teams")
        for x in range(nrOfTeams):
            self.teams.append(Team(nfl_list[x].split()[0], nfl_list[x].split()[1]))