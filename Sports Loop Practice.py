#Michael Coleman
#July 2026

team_name = input(" Enter the team name: ")
wins = int(input(" Enter the number of wins: "))
losses = int(input(" Enter the number of losses: "))
Points_Per_Game = int(input(" Enter the number of points scored per game: "))
division_name = input(" Enter the division name: ")
division_winner = input(" Did this team win their division (Yes/No): ")
made_playoffs = input(" Did this team make the playoffs (Yes/No): ")

winning_percentage = wins / (wins + losses) * 100

print(f"__________________________________")
print(f" TEAM REPORT")
print(f"__________________________________")
print()
print(f"{team_name} {wins} - {losses} ({winning_percentage:.1f}%)")
if winning_percentage >= 65:
    print(f"{team_name} have a winning percentage of {winning_percentage:.0f}% and had a very successful season this year.")
elif winning_percentage < 50:
    print(f"{team_name} have a winning percentage of {winning_percentage:.0f}% and struggled during this season.")
elif winning_percentage >= 50 and winning_percentage < 65:
    print(f"{team_name} have a winning percentage of {winning_percentage:.0f}% and had an average season this year.")

if division_winner == "Yes" or division_winner == "yes":
    print(f"{team_name} won the {division_name} division!")
if division_winner == "No" or division_winner == "no":
    print(f"{team_name} did not win the {division_name} division.")

if made_playoffs == "Yes" or made_playoffs == "yes":
    print(f"{team_name} made the playoffs!")
if made_playoffs == "No" or made_playoffs == "no":
    print(f"{team_name} did not make the playoffs.")

if made_playoffs == made_playoffs.lower() == "Yes" and division_winner == division_winner.lower() == "Yes" :
    print(f"The {team_name} is a top team in the NBA this year.")
    print(f"The {team_name} made the playoffs and won the {division_name} division.")

if made_playoffs == "No" or made_playoffs == "no" and division_winner == "No" or division_winner == "no":
    print(f"The {team_name} struggled during this season and will have a top pick in the NBA draft this year.")
    print(f"The {team_name} did not make the playoffs and did not win the {division_name} division.")


print(f"{team_name} scored {Points_Per_Game} points per game this season.")

