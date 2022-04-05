from asyncio.windows_events import NULL


class Player:
    def __init__(self, first_name, last_name, team=None):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

    def __str__(self):
        return "{}, {} : {}".format(self.last_name, self.first_name, self.team)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def first_name(self):
        return self.first_name
    
    def last_name(self):
        return self.last_name

    def get_current_team(self):
        return self.team

    def set_current_team(self, team):
        self.team = team
