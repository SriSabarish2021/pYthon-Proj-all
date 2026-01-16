import random
get_start=input("Enter to Start the game: ")
while True:
    
    random_num=random.randint(1,6)
    print(f"Dice Number is: {random_num}")
    get_play_again=input("Wana Play Again(y,n): ")
    if get_play_again=='n':
        print("Thank You ")
        break

