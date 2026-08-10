#NFL Comparisons
#Michael Coleman


wins = 12
losses = 5

winning_record = wins > losses
made_playoffs = True
team1 = "Los Angeles Rams"
games_played = 17
successful_season =  made_playoffs and winning_record
division_winner = True

if made_playoffs:
    print(f"{team1} clinched a playoff berth.")
else:
    print(f"{team1} missed the playoffs.")

if division_winner:
    print(f"{team1} won their division.")
else:
    print(f"{team1} did not win their division.")

if wins < 4:
    print(f"{team1} is in contention for the #1 overall pick.")
elif not winning_record or not made_playoffs:
    print(f" {team1} will have a top 15 draft pick.")
else:
    print(f" The {team1} will have a late round draft pick.")
    


if winning_record:
    print(f"{team1} finished above .500.")
elif wins == wins:
    print(f" {team1} finished at .500.")
else:
    print(f"{team1} finished below .500.")

if winning_record and made_playoffs:
    print(f" {team1} had a a successful season.")
else:
    print(f"{team1} did not have a successful season.")



