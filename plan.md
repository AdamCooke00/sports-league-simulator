# Plan for Sports Simulator

## Goals of Project
- Simulate NFL Season
- Predict Winners of Games
- In-depth prediction that involves true players and schedules
- Be able to swap players on rosters and get a true prediction on how well the team would play with that roster


## Code Plan

### Global Functions

>Returns ordered Team_List based on records of teams
- *get_division_standings([*Division*])*
  - *returns [Team_List]*

>Returns ordered Team_List based on records of teams taking into account divisional leaders
- *get_conference_standings([*Conference*])*
  - *returns [Team_List]*
  - Plan
    - get all divison standings
    - take top team from each division and order them
    - take the rest of the teams and order them
    - put lists together

>Returns Game_List for playoff games based on end of season standings
- *get_playoff_schedule([Season])*
  - *returns False if Completed=True | Playoffs = Completed | Season != Completed*
  - *returns [Game_List]*
  - Plan
    - get conference standings
    - generate schedule from standings

### Objects

#### Player
- Position [Enum]
- Team [Object]
- Injured [Boolean]
- Name [String]

#### Game
- Played [Boolean]
- Home [Team]
- Away [Team]
- Winner [Home/Away]
- Loser [Home/Away]
- Score [Score]

>Choose Winner. Choose Loser. Choose Score. Update Team Records
- *simulate()*

#### Team
- Roster [Player_List]
- Schedule [Game_List]
- Wins [Int]
- Losses [Int]
- GamesPlayed [Int]
- GamesRemaining [Int]
- Name [String]
- Division [Division]
- Conference [Conference]

>Returns tuple (wins,losses)
- *get_record()*

>Generates fake players and adds to roster
- *generate_roster()*
  
#### Division
- Name [String]
- Teams [Team_List]

#### Conference
- Name [String]
- Teams [Team_List]
- Divisions [Division_List]

#### Season
- Year [Year]
- Completed [Boolean]
- Regular_Season_Completed [Boolean]
- Playoffs_Completed [Boolean]
- Champion [Team]
- GamesPerTeam [Int]
- Schedule [Game_List]
- Playoff_Schedule [Game_List]
- Teams [Team_List]
- Conferences [Conference_List]
- Divisions [Division_List]

>Generates all games in a season
- *generate_schedule()*

>Generates all teams and adds them to respective objects
- *generate_teams()*

>Simulates all games in a season
- *simulate()*

#### League
- Name [String]
- Seasons [Season_List]