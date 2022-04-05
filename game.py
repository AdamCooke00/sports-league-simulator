import random
class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.winner = None
        self.loser = None

    def __str__(self):
        return "Home: {}\nAway: {}\n{} def. {}".format(self.home_team, self.away_team, self.winner, self.loser)

    def simulate(self):
        rnd = random.randint(0, 1)
        self.winner = self.home_team if rnd else self.away_team
        self.loser = self.away_team if rnd else self.home_team
        self.winner.add_win()
        self.loser.add_loss()
    
    def get_home_team(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team
    def get_winner(self):
        return self.winning
    def get_loser(self):
        return self.loser