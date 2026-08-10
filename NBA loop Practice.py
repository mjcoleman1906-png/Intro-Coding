#Michael COleman
#July 2026


nba_teams = [
    "Los Angeles Lakers", #1
    "Golden State Warriors", #2
    "Los Angeles Clippers", #3
    "Denver Nuggets", #4
    "Detroit Pistons", #5
    "Boston Celtics",  #6
    "Milwaukee Bucks", #7
    "Miami Heat", #8
    "Phoenix Suns", #9
    "Utah Jazz", #10
    "Dallas Mavericks", #11
    "Houston Rockets", #12
    "New York Knicks", #13
    "Brooklyn Nets", #14
    "Chicago Bulls", #15
    "Charlotte Hornets", #16
    "Atlanta Hawks", #17
    "Indiana Pacers", #18
    "Orlando Magic", #19
    "Washington Wizards", #20
    "Minnesota Timberwolves", #21
    "New Orleans Pelicans", #22
    "Portland Trail Blazers", #23
    "Sacramento Kings", #24
    "San Antonio Spurs", #25
    "Oklahoma City Thunder", #26
    "Memphis Grizzlies", #27
    "Toronto Raptors", #28
    "Cleveland Cavaliers", #29
    "Philadelphia 76ers", #30
]
for i in range(len(nba_teams)):
    team = nba_teams[i]

Western_Conference_Teams = [
    "Los Angeles Lakers",
    "Golden State Warriors",
    "Los Angeles Clippers",
    "Denver Nuggets",
    "Phoenix Suns",
    "Utah Jazz",
    "Dallas Mavericks",
    "Houston Rockets",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Oklahoma City Thunder",
    "Memphis Grizzlies",
    "Minnesota Timberwolves",
    "Portland Trail Blazers",
    "New Orleans Pelicans"
]

Eastern_Conference_Teams = [
    "Detroit Pistons",
    "Boston Celtics",
    "Milwaukee Bucks",
    "Miami Heat",
    "New York Knicks",
    "Brooklyn Nets",
    "Chicago Bulls",
    "Charlotte Hornets",
    "Atlanta Hawks",
    "Indiana Pacers",
    "Orlando Magic",
    "Washington Wizards",
    "Toronto Raptors",
    "Cleveland Cavaliers",
    "Philadelphia 76ers"
]
Atlantic_Division_Teams = [
    "Boston Celtics",
    "Brooklyn Nets",
    "New York Knicks",
    "Philadelphia 76ers",
    "Toronto Raptors"
]
Central_Division_Teams = [
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Detroit Pistons",
    "Indiana Pacers",
    "Milwaukee Bucks"
]
Southeast_Division_Teams = [
    "Atlanta Hawks",
    "Charlotte Hornets",
    "Miami Heat",
    "Orlando Magic",
    "Washington Wizards"
]
Northwest_Division_Teams = [
    "Denver Nuggets",
    "Minnesota Timberwolves",
    "Oklahoma City Thunder",
    "Portland Trail Blazers",
    "Utah Jazz"
]
Pacific_Division_Teams = [
    "Golden State Warriors",        
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Phoenix Suns",
    "Sacramento Kings"
]
Southwest_Division_Teams = [
    "Dallas Mavericks",
    "Houston Rockets",
    "Memphis Grizzlies",
    "New Orleans Pelicans",
    "San Antonio Spurs"
]

Nba_teams_points_per_game_25_26 = [
    116.3,
    114.6,
    113.8,
    122.1,
    117.8,
    114.9,
    110.6,
    120.9,
    112.6,
    117.6,
    114.1,
    115.2,
    116.5,
    105.9,
    116.3,
    116.0,
    118.5,
    112.4,
    115.7,
    112.9,
    118.0,
    115.5,
    115.5,
    111.0,
    119.8,
    119.0,
    114.7,
    114.6,
    119.5,
    115.9
]
nba_team_home_record_25_26 = [
    "28-13",
  "22-19",
  "23-18",
  "28-13",
  "31-9",
  "30-11",
  "19-22",
  "26-15",
  "25-16",
  "14-27",
  "16-25",
  "30-11",
  "30-10",
  "12-29",
  "18-23",
  "21-20",
  "24-17",
  "11-30",
  "25-15",
  "11-30",
  "26-15",
  "17-24",
  "24-17",
  "15-26",
  "32-8",
  "34-7",
  "13-27",
  "24-17",
  "27-14",
  "23-18"
]

nba_team_away_record_25_26 = [
    "25-16",
    "15-26",
    "19-22",
    "26-15",
    "28-13",
    "26-15",
    "13-28",
    "17-24",
    "20-21",
    "8-33",
    "10-30",
    "22-19",
    "22-19",
    "8-33",
    "13-28",
    "23-18",
    "22-19",
    "8-33",
    "19-20",
    "6-35",
    "23-18",
    "9-32",
    "18-23",
    "7-34",
    "29-12",
    "30-10",
    "11-29",
    "22-19",
    "25-16",
    "22-19"
]

nba_team_division_record_25_26 = [
    "10-7",
    "7-9",
    "10-6",
    "11-5",
    "12-4",
    "10-6",
    "9-7",
    "10-7",
    "10-7",
    "1-15",
    "4-12",
    "10-6",
    "14-3",
    "3-13",
    "4-12",
    "11-5",
    "9-7",
    "4-12",
    "9-8",
    "2-14",
    "9-7",
    "7-9",
    "7-9",
    "4-12",
    "13-3",
    "12-4",
    "6-10",
    "5-12",
    "11-5",
    "9-7"
]

nba_team_conference_record_25_26 = [
    "33-19",
    "24-28",
    "25-27",
    "36-16",
    "39-13",
    "36-16",
    "21-31",
    "27-25",
    "29-23",
    "12-40",
    "14-37",
    "29-23",
    "35-17",
    "14-37",
    "19-32",
    "26-26",
    "27-25",
    "15-37",
    "26-26",
    "11-41",
    "31-21",
    "17-34",
    "29-23",
    "14-38",
    "36-16",
    "41-11",
    "19-33",
    "33-19",
    "33-19",
    "27-25"
]

nba_team_offensive_rating_25_26 = [
    117.0,  # Los Angeles Lakers
    113.8,  # Golden State Warriors
    116.3,  # Los Angeles Clippers
    121.2,  # Denver Nuggets
    117.3,  # Detroit Pistons
    120.0,  # Boston Celtics
    112.2,  # Milwaukee Bucks
    115.8,  # Miami Heat
    114.2,  # Phoenix Suns
    112.7,  # Utah Jazz
    110.3,  # Dallas Mavericks
    117.5,  # Houston Rockets
    118.7,  # New York Knicks
    108.2,  # Brooklyn Nets
    112.1,  # Chicago Bulls
    118.4,  # Charlotte Hornets
    115.0,  # Atlanta Hawks
    110.1,  # Indiana Pacers
    114.2,  # Orlando Magic
    109.7,  # Washington Wizards
    115.6,  # Minnesota Timberwolves
    113.3,  # New Orleans Pelicans
    113.1,  # Portland Trail Blazers
    110.6,  # Sacramento Kings
    118.7,  # San Antonio Spurs
    117.6,  # Oklahoma City Thunder
    112.4,  # Memphis Grizzlies
    115.0,  # Toronto Raptors
    118.3,  # Cleveland Cavaliers
    114.3   # Philadelphia 76ers
]
nba_team_defensive_rating_25_26 = [
    115.5,  # Los Angeles Lakers
    114.4,  # Golden State Warriors
    115.2,  # Los Angeles Clippers
    116.0,  # Denver Nuggets
    108.9,  # Detroit Pistons
    111.7,  # Boston Celtics
    118.3,  # Milwaukee Bucks
    113.6,  # Miami Heat
    112.9,  # Phoenix Suns
    120.8,  # Utah Jazz
    115.5,  # Dallas Mavericks
    112.1,  # Houston Rockets
    112.3,  # New York Knicks
    118.2,  # Brooklyn Nets
    117.4,  # Chicago Bulls
    113.5,  # Charlotte Hornets
    112.9,  # Atlanta Hawks
    117.9,  # Indiana Pacers
    113.6,  # Orlando Magic
    121.5,  # Washington Wizards
    112.5,  # Minnesota Timberwolves
    117.6,  # New Orleans Pelicans
    113.5,  # Portland Trail Blazers
    120.3,  # Sacramento Kings
    110.4,  # San Antonio Spurs
    106.5,  # Oklahoma City Thunder
    118.4,  # Memphis Grizzlies
    112.1,  # Toronto Raptors
    114.1,  # Cleveland Cavaliers
    114.4   # Philadelphia 76ers
]
nba_team_opponent_points_per_game_25_26 = [
    114.6,
    115.2,
    112.6,
    116.9,
    109.6,
    107.2,
    116.8,
    118.5,
    111.1,
    126.0,
    119.6,
    110.0,
    110.1,
    115.9,
    121.5,
    111.2,
    116.0,
    120.4,
    115.1,
    124.9,
    114.6,
    120.0,
    115.8,
    121.0,
    111.5,
    107.9,
    120.7,
    111.8,
    115.4,
    116.1
]
nba_team_point_differential = [Nba_teams_points_per_game_25_26[i] - nba_team_opponent_points_per_game_25_26[i] for i in range(len(Nba_teams_points_per_game_25_26))]


nba_team_offensive_rebound_pct_25_26 = [
    28.5,  # Lakers
    30.2,  # Warriors
    28.4,  # Clippers
    28.6,  # Nuggets
    35.4,  # Pistons
    33.6,  # Celtics
    26.3,  # Bucks
    29.6,  # Heat
    33.1,  # Suns
    29.8,  # Jazz
    27.9,  # Mavericks
    38.8,  # Rockets
    32.8,  # Knicks
    28.7,  # Nets
    27.9,  # Bulls
    35.8,  # Hornets
    29.1,  # Hawks
    26.3,  # Pacers
    30.6,  # Magic
    28.5,  # Wizards
    30.2,  # Timberwolves
    31.1,  # Pelicans
    35.4,  # Trail Blazers
    29.8,  # Kings
    30.6,  # Spurs
    26.4,  # Thunder
    30.1,  # Grizzlies
    30.0,  # Raptors
    30.7,  # Cavaliers
    30.6,  # 76ers
]

nba_team_pace_played_25_26 = [
     99.22,   # Los Angeles Lakers
    100.05,  # Golden State Warriors
    97.29,   # LA Clippers
    99.49,   # Denver Nuggets
    99.88,   # Detroit Pistons
    95.58,   # Boston Celtics
    98.33,   # Milwaukee Bucks
    104.22,  # Miami Heat
    98.14,   # Phoenix Suns
    103.54,  # Utah Jazz
    102.62,  # Dallas Mavericks
    96.98,   # Houston Rockets
    97.71,   # New York Knicks
    97.60,   # Brooklyn Nets
    103.22,  # Chicago Bulls
    97.59,   # Charlotte Hornets
    102.50,  # Atlanta Hawks
    101.78,  # Indiana Pacers
    100.56,  # Orlando Magic
    102.49,  # Washington Wizards
    101.50,  # Minnesota Timberwolves
    101.37,  # New Orleans Pelicans
    101.63,  # Portland Trail Blazers
    100.12,  # Sacramento Kings
    100.72,  # San Antonio Spurs
    100.37,  # Oklahoma City Thunder
    101.69,  # Memphis Grizzlies
    99.22,   # Toronto Raptors
    100.70,  # Cleveland Cavaliers
    100.39,  # Philadelphia 76ers
]

nba_team_pie_rating_25_26 = [
    51.3,  # Los Angeles Lakers
    49.5,  # Golden State Warriors
    50.8,  # LA Clippers
    52.9,  # Denver Nuggets
    55.2,  # Detroit Pistons
    53.6,  # Boston Celtics
    46.4,  # Milwaukee Bucks
    51.4,  # Miami Heat
    49.5,  # Phoenix Suns
    46.4,  # Utah Jazz
    47.7,  # Dallas Mavericks
    53.3,  # Houston Rockets
    53.3,  # New York Knicks
    43.6,  # Brooklyn Nets
    48.0,  # Chicago Bulls
    51.6,  # Charlotte Hornets
    51.0,  # Atlanta Hawks
    46.5,  # Indiana Pacers
    50.5,  # Orlando Magic
    43.3,  # Washington Wizards
    51.6,  # Minnesota Timberwolves
    48.0,  # New Orleans Pelicans
    48.8,  # Portland Trail Blazers
    45.5,  # Sacramento Kings
    54.2,  # San Antonio Spurs
    56.2,  # Oklahoma City Thunder
    47.0,  # Memphis Grizzlies
    52.2,  # Toronto Raptors
    52.2,  # Cleveland Cavaliers
    49.7,  # Philadelphia 76ers
]

nba_teams_total_possessions_25_26 = [
    8156,  # Los Angeles Lakers
    8255,  # Golden State Warriors
    8019,  # LA Clippers
    8259,  # Denver Nuggets
    8231,  # Detroit Pistons
    7850,  # Boston Celtics
    8087,  # Milwaukee Bucks
    8561,  # Miami Heat
    8083,  # Phoenix Suns
    8558,  # Utah Jazz
    8484,  # Dallas Mavericks
    8042,  # Houston Rockets
    8046,  # New York Knicks
    8028,  # Brooklyn Nets
    8506,  # Chicago Bulls
    8033,  # Charlotte Hornets
    8444,  # Atlanta Hawks
    8377,  # Indiana Pacers
    8310,  # Orlando Magic
    8442,  # Washington Wizards
    8372,  # Minnesota Timberwolves
    8363,  # New Orleans Pelicans
    8370,  # Portland Trail Blazers
    8233,  # Sacramento Kings
    8275,  # San Antonio Spurs
    8301,  # Oklahoma City Thunder
    8365,  # Memphis Grizzlies
    8177,  # Toronto Raptors
    8286,  # Cleveland Cavaliers
    8314,  # Philadelphia 76ers
]

nba_team_rebound_pct_25_26 = [
    49.9,  # Los Angeles Lakers
    49.0,  # Golden State Warriors
    49.0,  # LA Clippers
    51.1,  # Denver Nuggets
    52.4,  # Detroit Pistons
    52.5,  # Boston Celtics
    48.2,  # Milwaukee Bucks
    49.9,  # Miami Heat
    49.8,  # Phoenix Suns
    49.2,  # Utah Jazz
    49.2,  # Dallas Mavericks
    54.5,  # Houston Rockets
    52.2,  # New York Knicks
    47.8,  # Brooklyn Nets
    49.6,  # Chicago Bulls
    53.9,  # Charlotte Hornets
    49.5,  # Atlanta Hawks
    47.5,  # Indiana Pacers
    50.5,  # Orlando Magic
    47.1,  # Washington Wizards
    49.9,  # Minnesota Timberwolves
    49.1,  # New Orleans Pelicans
    51.7,  # Portland Trail Blazers
    48.7,  # Sacramento Kings
    52.1,  # San Antonio Spurs
    49.0,  # Oklahoma City Thunder
    47.8,  # Memphis Grizzlies
    49.6,  # Toronto Raptors
    50.2,  # Cleveland Cavaliers
    49.1,  # Philadelphia 76ers
]

nba_team_turnover_pct_25_26 = [
    14.6,  # Los Angeles Lakers
    15.6,  # Golden State Warriors
    14.7,  # LA Clippers
    12.8,  # Denver Nuggets
    15.1,  # Detroit Pistons
    12.9,  # Boston Celtics
    15.4,  # Milwaukee Bucks
    13.1,  # Miami Heat
    14.7,  # Phoenix Suns
    14.9,  # Utah Jazz
    14.1,  # Dallas Mavericks
    15.7,  # Houston Rockets
    13.9,  # New York Knicks
    16.1,  # Brooklyn Nets
    14.8,  # Chicago Bulls
    15.7,  # Charlotte Hornets
    13.8,  # Atlanta Hawks
    14.2,  # Indiana Pacers
    14.0,  # Orlando Magic
    15.2,  # Washington Wizards
    14.5,  # Minnesota Timberwolves
    13.9,  # New Orleans Pelicans
    16.9,  # Portland Trail Blazers
    14.3,  # Sacramento Kings
    13.3,  # San Antonio Spurs
    12.4,  # Oklahoma City Thunder
    14.8,  # Memphis Grizzlies
    13.7,  # Toronto Raptors
    13.8,  # Cleveland Cavaliers
    13.4,  # Philadelphia 76ers
]

nba_team_effective_field_goal_percentage_25_26 = [
    57.3,  # Los Angeles Lakers
    54.9,  # Golden State Warriors
    55.9,  # LA Clippers
    57.7,  # Denver Nuggets
    54.6,  # Detroit Pistons
    55.3,  # Boston Celtics
    56.5,  # Milwaukee Bucks
    54.2,  # Miami Heat
    53.7,  # Phoenix Suns
    53.6,  # Utah Jazz
    52.7,  # Dallas Mavericks
    54.2,  # Houston Rockets
    55.7,  # New York Knicks
    52.0,  # Brooklyn Nets
    54.7,  # Chicago Bulls
    55.2,  # Charlotte Hornets
    55.4,  # Atlanta Hawks
    53.3,  # Indiana Pacers
    53.1,  # Orlando Magic
    53.5,  # Washington Wizards
    55.9,  # Minnesota Timberwolves
    52.7,  # New Orleans Pelicans
    53.4,  # Portland Trail Blazers
    52.5,  # Sacramento Kings
    55.9,  # San Antonio Spurs
    56.1,  # Oklahoma City Thunder
    53.3,  # Memphis Grizzlies
    54.6,  # Toronto Raptors
    56.1,  # Cleveland Cavaliers
    53.0,  # Philadelphia 76ers
]
nba_team_true_shooting_percentage_25_26 = [
     60.9,  # Los Angeles Lakers
    58.4,  # Golden State Warriors
    60.2,  # LA Clippers
    61.6,  # Denver Nuggets
    58.3,  # Detroit Pistons
    58.3,  # Boston Celtics
    58.9,  # Milwaukee Bucks
    58.0,  # Miami Heat
    56.8,  # Phoenix Suns
    57.5,  # Utah Jazz
    56.4,  # Dallas Mavericks
    57.6,  # Houston Rockets
    59.0,  # New York Knicks
    55.9,  # Brooklyn Nets
    58.0,  # Chicago Bulls
    58.9,  # Charlotte Hornets
    58.4,  # Atlanta Hawks
    56.8,  # Indiana Pacers
    57.6,  # Orlando Magic
    56.6,  # Washington Wizards
    59.2,  # Minnesota Timberwolves
    56.8,  # New Orleans Pelicans
    57.0,  # Portland Trail Blazers
    56.0,  # Sacramento Kings
    59.5,  # San Antonio Spurs
    59.9,  # Oklahoma City Thunder
    57.0,  # Memphis Grizzlies
    58.1,  # Toronto Raptors
    59.5,  # Cleveland Cavaliers
    57.2,  # Philadelphia 76ers
]

nba_team_defensive_rebound_pct_25_26 = [
    70.0,  # Lakers
    68.4,  # Warriors
    68.1,  # Clippers
    71.7,  # Nuggets
    68.9,  # Pistons
    71.0,  # Celtics
    69.5,  # Bucks
    70.3,  # Heat
    67.7,  # Suns
    69.3,  # Jazz
    70.2,  # Mavericks
    70.1,  # Rockets
    71.5,  # Knicks
    68.7,  # Nets
    70.8,  # Bulls
    72.2,  # Hornets
    70.2,  # Hawks
    69.5,  # Pacers
    71.0,  # Magic
    66.4,  # Wizards
    69.1,  # Timberwolves
    67.4,  # Pelicans
    68.8,  # Trail Blazers
    68.5,  # Kings
    72.4,  # Spurs
    69.7,  # Thunder
    66.3,  # Grizzlies
    69.3,  # Raptors
    69.2,  # Cavaliers
    67.8,  # 76ers
]

nba_team_wins_25_26 = [
    53,
    37,
    42,
    54,
    60,
    56,
    32,
    43,
    45,
    22,
    26,
    52,
    53,
    20,
    31,
    44,
    46,
    19,
    45,
    17,
    49,
    26,
    42,
    22,
    62,
    64,
    25,
    46,
    52,
    45
]

nba_team_losses_25_26 = [
    29,
    45,
    40,
    28,
    22,
    26,
    50,
    39,
    37,
    60,
    56,
    30,
    29,
    62,
    51,
    38,
    36,
    63,
    37,
    65,
    33,
    56,
    40,
    60,
    20,
    18,
    57,
    36,
    30,
    37
]
nba_teams_ast_to_ratio = [
    1.79,  # Los Angeles Lakers
    1.85,  # Golden State Warriors
    1.66,  # Los Angeles Clippers
    2.25,  # Denver Nuggets
    1.84,  # Detroit Pistons
    1.99,  # Boston Celtics
    1.70,  # Milwaukee Bucks
    2.12,  # Miami Heat
    1.70,  # Phoenix Suns
    1.91,  # Utah Jazz
    1.74,  # Dallas Mavericks
    1.65,  # Houston Rockets
    2.01,  # New York Knicks
    1.59,  # Brooklyn Nets
    1.86,  # Chicago Bulls
    1.71,  # Charlotte Hornets
    2.13,  # Atlanta Hawks
    1.91,  # Indiana Pacers
    1.87,  # Orlando Magic
    1.60,  # Washington Wizards
    1.76,  # Minnesota Timberwolves
    1.77,  # New Orleans Pelicans
    1.46,  # Portland Trail Blazers
    1.78,  # Sacramento Kings
    2.09,  # San Antonio Spurs
    2.05,  # Oklahoma City Thunder
    1.85,  # Memphis Grizzlies
    2.16,  # Toronto Raptors
    2.02,  # Cleveland Cavaliers
    1.81   # Philadelphia 76ers
]

nba_teams_assist_ratio_25_26 = [
    18.7,  # Los Angeles Lakers
    20.0,  # Golden State Warriors
    17.7,  # Los Angeles Clippers
    20.3,  # Denver Nuggets
    19.1,  # Detroit Pistons
    18.0,  # Boston Celtics
    18.9,  # Milwaukee Bucks
    19.5,  # Miami Heat
    17.6,  # Phoenix Suns
    19.9,  # Utah Jazz
    17.7,  # Dallas Mavericks
    17.8,  # Houston Rockets
    19.4,  # New York Knicks
    18.3,  # Brooklyn Nets
    19.5,  # Chicago Bulls
    18.6,  # Charlotte Hornets
    20.4,  # Atlanta Hawks
    19.4,  # Indiana Pacers
    18.6,  # Orlando Magic
    17.6,  # Washington Wizards
    18.3,  # Minnesota Timberwolves
    17.6,  # New Orleans Pelicans
    17.3,  # Portland Trail Blazers
    18.2,  # Sacramento Kings
    19.5,  # San Antonio Spurs
    18.5,  # Oklahoma City Thunder
    19.2,  # Memphis Grizzlies
    20.5,  # Toronto Raptors
    19.7,  # Cleveland Cavaliers
    17.4   # Philadelphia 76ers
]
nba_team_net_rating_25_26 = [
    1.5,    # Los Angeles Lakers
    -0.5,   # Golden State Warriors
    1.1,    # Los Angeles Clippers
    5.2,    # Denver Nuggets
    8.4,    # Detroit Pistons
    8.3,    # Boston Celtics
    -6.1,   # Milwaukee Bucks
    2.1,    # Miami Heat
    1.4,    # Phoenix Suns
    -8.2,   # Utah Jazz
    -5.2,   # Dallas Mavericks
    5.4,    # Houston Rockets
    6.4,    # New York Knicks
    -10.0,  # Brooklyn Nets
    -5.3,   # Chicago Bulls
    4.9,    # Charlotte Hornets
    2.2,    # Atlanta Hawks
    -7.8,   # Indiana Pacers
    0.6,    # Orlando Magic
    -11.8,  # Washington Wizards
    3.1,    # Minnesota Timberwolves
    -4.4,   # New Orleans Pelicans
    -0.4,   # Portland Trail Blazers
    -9.7,   # Sacramento Kings
    8.4,    # San Antonio Spurs
    11.1,   # Oklahoma City Thunder
    -6.0,   # Memphis Grizzlies
    2.9,    # Toronto Raptors
    4.1,    # Cleveland Cavaliers
    -0.1    # Philadelphia 76ers
]

nba_teams_ast_pct_25_26 = [
    61.5,   # Los Angeles Lakers
    70.6,   # Golden State Warriors
    58.6,   # Los Angeles Clippers
    66.5,   # Denver Nuggets
    64.1,   # Detroit Pistons
    58.5,   # Boston Celtics
    63.3,   # Milwaukee Bucks
    66.3,   # Miami Heat
    60.1,   # Phoenix Suns
    69.6,   # Utah Jazz
    60.4,   # Dallas Mavericks
    59.1,   # Houston Rockets
    64.3,   # New York Knicks
    66.8,   # Brooklyn Nets
    67.2,   # Chicago Bulls
    64.3,   # Charlotte Hornets
    69.1,   # Atlanta Hawks
    67.8,   # Indiana Pacers
    64.7,   # Orlando Magic
    59.9,   # Washington Wizards
    61.2,   # Minnesota Timberwolves
    59.6,   # New Orleans Pelicans
    61.6,   # Portland Trail Blazers
    61.5,   # Sacramento Kings
    64.6,   # San Antonio Spurs
    59.8,   # Oklahoma City Thunder
    67.3,   # Memphis Grizzlies
    69.2,   # Toronto Raptors
    65.3,   # Cleveland Cavaliers
    58.9    # Philadelphia 76ers
]

wins = nba_team_wins_25_26[i]
losses = nba_team_losses_25_26[i]
def calculate_winning_percentage(wins, losses):
        total_games = wins + losses
        if total_games == 0:
            return 0.0
        return (wins / total_games) * 100




def team_grade(winning_percentage):
    if winning_percentage >= 70:
        return "A"
    elif winning_percentage >= 60:
        return "B"
    elif winning_percentage >= 45:
        return "C"
    elif winning_percentage >= 30:
        return "D"
    else:
        return "F"
    
for i in range(len(nba_teams)):
    team = nba_teams[i]
    wins = nba_team_wins_25_26[i]
    losses = nba_team_losses_25_26[i]
    net_rating = nba_team_net_rating_25_26[i]
    point_differential = nba_team_point_differential[i]
    offensive_rating = nba_team_offensive_rating_25_26[i]
    defensive_rating = nba_team_defensive_rating_25_26[i]

    winning_percentage = calculate_winning_percentage(wins, losses)
    grade = team_grade(winning_percentage)

    if point_differential > 0:
        team_quality = "good team"
    elif point_differential < 0:
        team_quality = "below-average team"
    else:
        team_quality = "even team"

    if offensive_rating > defensive_rating:
        team_style = "offense-led"
    else:
        team_style = "defense-led"

    if offensive_rating >= 116.5:
        offense_level = "elite offense"
    elif offensive_rating >= 113.0:
        offense_level = "above-average offense"
    else:
        offense_level = "below-average offense"

    print("=" * 60)
    print(
        f"{team} | "
        f"{wins}-{losses} | "
        f"Win%: {winning_percentage:.1f}% | "
        f"Net Rating: {net_rating:+.1f}"
    )
    print(f"Profile: {team_quality}, {team_style}, {offense_level}")
    print(f" The {nba_teams[i]} earned a {grade} for their performance in the 2025-2026 season.")
    print()





    
