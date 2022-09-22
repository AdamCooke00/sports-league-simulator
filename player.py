from asyncio.windows_events import NULL
from contextlib import nullcontext


class Player:
    def __init__(self, first_name, last_name, injured=False, position=None, team=None):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.injured = injured
        self.position = position 

    def __str__(self):
        if self.team is None:
            return "Player: {}, {}.\nStatus: Free Agent".format(self.last_name, self.first_name)
        return "Player: {}, {}\nTeam: {}".format(self.last_name, self.first_name, self.team)

    def __repr__(self):
        return f"Player('{self.first_name}', '{self.last_name}', {repr(self.team)}"


