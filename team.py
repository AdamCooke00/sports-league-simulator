import names
from player import Player

class Team:
    def __init__(self, city, nickname, generate_roster=(False, 0)):
        self.city = city
        self.nickname = nickname
        self.wins = 0
        self.losses = 0
        self.schedule = []
        self.roster = []
        self.games_remaining = 0
        self.games_played = 0
        self.divison = None
        self.conference = None
        
        if generate_roster[0] is True:
            if generate_roster[1] < 1:
                raise Exception("Cannot generate roster of {} players".format(generate_roster[1]))
            self.generate_roster(generate_roster[1])

    def __repr__(self):
        return "Team: {} {}\nGP: {}\nGR: {}\nRecord: {}-{}\n".format(self.city, self.nickname, self.games_played, self.games_remaining, self.wins, self.losses)

    def team_name(self):
        return self.city + " " + self.nickname

    def get_record(self):
        return (self.wins, self.losses)

    def generate_roster(self, nrOfPlayers):
        if nrOfPlayers < 1:
            raise Exception(f"Unable to generate roster of size {nrOfPlayers}")
        self.active_roster = []
        for _ in range(nrOfPlayers):
            self.active_roster.append(Player(names.get_full_name().split()[0], names.get_full_name().split()[1], self))

