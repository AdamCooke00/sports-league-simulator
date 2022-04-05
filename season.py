import random
from game import Game
from team import Team

class Season():
    def __init__(self, year, games_per_team, league_name, champion=None):
        self.year = year
        self.games_per_team = games_per_team
        self.league_name = league_name
        self.champion = champion
        self.team_list = []
        self.standings = []

    def __str__(self):
        return "{} {} : {} Games per team.".format(self.league_name, self.year, self.games_per_team)

    def get_champion(self):
        return self.champion

    def generate_schedule(self):
        games = []
        if len(self.team_list) % 2 or len(self.team_list) < 1:
            raise Exception("Sorry, cannot make a schedule with odd number of teams.")
        for y in range(self.games_per_team):
            random.shuffle(self.team_list)
            for x in range(len(self.team_list)//2):
                genGame = Game(self.team_list[x*2], self.team_list[x*2+1])
                games.append(genGame)
                self.team_list[x*2].add_game_to_schedule(genGame)
                self.team_list[x*2+1].add_game_to_schedule(genGame)
        print("Schedules have been generated")
        self.games = games

    def simulate(self):
        for game in self.games:
            game.simulate()
        self.standings = sorted(self.team_list, key=lambda x: x.wins, reverse=True)
        self.champion = self.standings[0]

    def display_standings(self):
        for team in self.standings:
            wins, losses = team.get_record()
            print(team.get_name() + ": {}-{}".format(wins, losses))

    def generate_teams(self, nrOfTeams):
        self.team_list = []
        nfl_list = ["Arizona Cardinals","Atlanta Falcons","Baltimore Ravens","Buffalo Bills","Carolina Panthers","Chicago Bears","Cincinnati Bengals","Cleveland Browns","Dallas Cowboys","Denver Broncos","Detroit Lions","GreenBay Packers","Houston Texans","Indianapolis Colts","Jacksonville Jaguars","KansasCity Chiefs","LasVegas Raiders","LosAngeles Chargers","LosAngeles Rams","Miami Dolphins","Minnesota Vikings","NewEngland Patriots","NewOrleans Saints","NewYork Giants","NewYork Jets","Philadelphia Eagles","Pittsburgh Steelers","SanFrancisco 49ers","Seattle Seahawks","TampaBay Buccaneers","Tennessee Titans","Washington Commanders"]
        if nrOfTeams > len(nfl_list):
            raise Exception("Too many teams")
        for x in range(nrOfTeams):
            self.team_list.append(Team(nfl_list[x].split()[0], nfl_list[x].split()[1]))
        self.standings = self.team_list[:]
