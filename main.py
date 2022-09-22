import random
from season import Season
from league_structures import League
from league_structures import display_standings
from player import Player
from team import Team


random.seed(50)

firstLeague = League("The National Football League")
print(firstLeague)
seasonOne = Season(2023, 17)
firstLeague.seasons.append(seasonOne)


seasonOne.generate_teams(32)
seasonOne.generate_schedule()
seasonOne.simulate()
display_standings(seasonOne.teams)


