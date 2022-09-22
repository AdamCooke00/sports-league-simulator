import random
class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.played = False
        self.winner = None
        self.loser = None
        self.score = None
        self.tie_game = False

    def __repr__(self):
        if self.played and self.tie_game is False:
            return "{} def. {}\nScore: {}".format(self.winner, self.loser, self.score)
        if self.played and self.tie_game:
            return "{} ties. {}\nScore: {}".format(self.home_team, self.away_team, self.score)
        if self.played is False:
            return "{} vs. {}".format(self.home_team, self.away_team)

    def simulate(self):
        rnd = random.randint(0, 1)
        if rnd:
            self.winner = self.home_team
            self.loser = self.away_team
        else:
            self.winner = self.away_team
            self.loser = self.home_team
        self.winner.wins+=1
        self.loser.losses+=1
        self.score = "14-7"
        self.played = True
