import random
from season import Season


random.seed(53)

firstSeason = Season(2022, 16, "NFL")
print(firstSeason)

firstSeason.generate_teams(32)
firstSeason.generate_schedule()
firstSeason.simulate()
firstSeason.display_standings()
