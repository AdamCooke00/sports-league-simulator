import names
from player import Player

class Team:
    def __init__(self, city, nickname, generate_roster=(True, 10)):
        self.city = city
        self.nickname = nickname
        self.wins = 0
        self.losses = 0
        self.schedule = []
        self.active_roster = []
        
        if generate_roster[0] is True:
            self.active_roster = self.generate_roster(generate_roster[1])

    def __str__(self):
        return "{} {}: ({}-{})".format(self.city, self.nickname, self.wins, self.losses)

    def get_name(self):
        return self.city + " " + self.nickname

    def get_active_roster(self):
        return self.active_roster

    def get_record(self):
        return (self.wins, self.losses)

    def get_schedule(self):
        return self.schedule

    def add_win(self):
        self.wins+=1

    def add_loss(self):
        self.losses+=1

    def add_game_to_schedule(self, game):
        self.schedule.append(game)

    def generate_roster(self, nrOfPlayers):
        roster_list = []
        for _ in range(nrOfPlayers):
            roster_list.append(Player(names.get_full_name().split()[0], names.get_full_name().split()[1], self.get_name()))
        return roster_list


