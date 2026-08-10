#lesson 6
# Michael Coleman

nfc_west_division = [
    "Rams",
    "Seahawks",
    "49ers",
    "Cardinals"
]

nfc_east_division = [
    "Giants",
    "Cowboys",
    "Eagles",
    "Commanders"
]

nfc_south_division = [
    "Falcons",
    "Panthers",
    "Saints",
    "Buccaneers"
]
nfc_north_division = [
    "Bears",
    "Packers",
    "Lions",
    "Vikings"
]

afc_east_division = [
    "Bills",
    "Dolphins",
    "Jets",
    "Patriots"
]
afc_south_division = [
    "Titans",
    "Colts",
    "Jaguars",
    "Texans"
]
afc_west_division = [
    "Chargers",
    "Cheifs",
    "Raiders",
    "Broncos"
]
afc_north_division = [
    "Bengals",
    "Browns",
    "Ravens",
    "Steelers"
]
teams = [
    "Rams",
    "Seahawks",
    "49ers",
    "Cardinals",
    "Giants",
    "Chargers",
    "Cheifs",
    "Colts",
    "Dolphins",
    "Bills",
    "Bengals",
    "Browns",
    "Jets"

]

wins = [
    12,
    14,
    12,
    3,
    4,
    11,
    6,
    8,
    7,
    12,
    6,
    5,
    3
]
teams.append("Cowboys")
teams.append("Bears")
teams.append("Packers")
teams.append("Lions")
teams.append("Vikings")
teams.append("Falcons")
teams.append("Panthers")
teams.append("Saints")
teams.append("Buccaneers")
teams.append("Titans")
teams.append("Raiders")
teams.append("Broncos")
teams.append("Jaguars")
teams.append("Eagles")
teams.append("Commanders")
teams.append("Texans")
teams.append("Patriots")


print(f" The {teams[5]} have {wins[5]} wins this season.")
print(f" The {teams[12]} have {wins[12]} wins this season.")
print(f" The {teams[3]} have {wins[3]} wins this season.")

print()
print(len(teams))