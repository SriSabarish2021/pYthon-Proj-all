print("Welcome To PIG Game".center(50,'-'))
print("")
get_no_of_players=int(input("Enter the Number of Players: "))
print("")
print(f"Total Players were {get_no_of_players}")
print("")
print("Lets Get in to the PIG Game")

for i in range(get_no_of_players):
    player_total=f"Player {i+1}"
    win=True

