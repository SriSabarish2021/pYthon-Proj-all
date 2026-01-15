import random
import threading
import time
print("Welcome TO Math Game")
array_operation=['+','-','*','/']
count=0
def game_strt():
    global array_operation
    get_started=input("Lets Start the Game(y,n): ").lower().strip()
    game=False
    if get_started=='y':
        game=True
    elif get_started=='n':
        game=False
        print("Thank You For Playing")
    else:
        print("Please Enter the Valid Input")
        return game_strt()
    while game:
        strt_time=time.time()
        for i in range(1,16):        
            def get_usr_inp():  
                try:
                    get_answer=int(input(f"{i}: Enter Answer :{random.randint(1,10)} {random.choice(array_operation)} {random.randint(1,10)}: "))
                except:
                    print("You Enter Invalid Input")
                    return get_usr_inp()
            get_usr_inp()
            if i==15:
                game=False

        end_time=time.time()
        total_time=f"{end_time-strt_time:.2f}"
        print(f"Total Time Take is {total_time}")
    

        


game_strt()