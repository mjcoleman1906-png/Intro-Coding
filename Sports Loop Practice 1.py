#Michael Coleman
#july 2026


nfc_west_teams = [
    "Rams",
    "Seahawks",
    "49ers",
    "Cardinals"
]

nfc_west_team_wins = [
    12,
    14,
    12,
    3
]

nfc_east_teams = [
    "Giants",
    "Cowboys",
    "Eagles",
    "Commanders"
]
nfc_east_team_wins = [
    4,
    7,
    11,
    5
]    

nfc_south_teams = [
    "Falcons",
    "Panthers",
    "Saints",
    "Buccaneers"
]
nfc_south_team_wins = [
    8,
    8,
    6,
    8
]
nfc_north_teams = [
    "Bears",
    "Packers",
    "Lions",
    "Vikings"
]
nfc_north_team_wins = [
    11,
    9,
    9,
    9
]

afc_east_teams = [
    "Bills",
    "Dolphins",
    "Jets",
    "Patriots",
]

afc_east_team_wins = [
    12,
    7,
    3,
    14
]

afc_south_teams = [
    "Titans",
    "Colts",
    "Jaguars",
    "Texans",
]

afc_south_team_wins = [
    3,
    8,
    13,
    12
]
afc_west_teams = [
    "Chargers",
    "Chiefs",
    "Raiders",
    "Broncos",
]
afc_west_team_wins = [
    11,
    6,
    3,
    14
]
afc_north_teams = [
    "Bengals",
    "Browns",
    "Ravens",
    "Steelers",
]
afc_north_team_wins = [
    6,
    5,
    8,
    10
]

# Combining lists
nfl_teams = (
    nfc_west_teams
    + nfc_east_teams
    + nfc_south_teams
    + nfc_north_teams
    + afc_east_teams
    + afc_south_teams
    + afc_west_teams
    + afc_north_teams
)

for team in afc_east_teams:
    print(f" {team} is a team in the AFC East.")

for team in afc_south_teams:
    print(f" {team} is a team in the AFC South.")

for team in afc_west_teams:
    print(f" {team} is a team in the AFC West.")

for team in afc_north_teams:
    print(f" The {team} are in the AFC North. ")

for team in nfc_west_teams:
    print(f" {team} is a team in the NFC West.")

for team in nfc_east_teams:
    print(f" {team} is a team in the NFC East.")

for team in nfc_south_teams:
    print(f" {team} is a team in the NFC South.")

for team in nfc_north_teams:
    print(f" {team} is a team in the NFC North.")


for i in range(len(afc_north_teams)):
    print(f"{afc_north_teams[i]} won {afc_north_team_wins[i]} games this season.")

for i in range(len(afc_west_teams)):
    print(f"{afc_west_teams[i]} won {afc_west_team_wins[i]} games this season.")

for i in range(len(afc_south_teams)):
    print(f"{afc_south_teams[i]} won {afc_south_team_wins[i]} games this season.")

for i in range(len(afc_east_teams)):
    print(f"{afc_east_teams[i]} won {afc_east_team_wins[i]} games this season.")