#Michael Coleman
# July 27th

def welcome_message():
    print("Welcome to the NBA Team Statistics Program!")

def favorite_team(team_name):
    print(f"Your favorite NBA team is the {team_name}.")

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def greet_user(name):
    print(f"Hello, {name}!")

def double(number):
    return number * 2
print(double(5))

def calculate_winning_percentage(wins, losses):
    total_games = wins + losses
    if total_games == 0:
        return 0.0
    return (wins / total_games) * 100

print(calculate_winning_percentage(53, 29))

double(5)

say_hello()
say_goodbye()
greet_user("Michael")
welcome_message()
favorite_team("Los Angeles Lakers")
