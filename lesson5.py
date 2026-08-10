#lesson 5 user input
#Michael Coleman

teams = []

team_name = input("Enter the team name: ")
wins = int(input("Enter the number of wins: "))
losses = int(input("Enter the number of losses: "))

winning_percentage = wins / (wins + losses) * 100

print()
print("Season Report")
print("__________________________________")
print("You entered: " )
print(f"Team Name: {team_name}")
print(f" Record: {wins}-{losses}")
print(f"Winning Percentage: {winning_percentage:.0f}%")
if winning_percentage >= 65:
    print(f"{team_name} has a winning percentage of {winning_percentage:.0f}% and had a very successful season this year.")
elif winning_percentage >= 50:
    print(f"{team_name} has a winning percentage of {winning_percentage:.0f}% and had an average season this year.")
else:
    print(f"{team_name} has a winning percentage of {winning_percentage:.0f}% and had a difficult season this year.")
