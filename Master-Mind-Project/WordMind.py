import random
print("Welcome to Color Guessing Game".center(50,"-"))
print("")
print("Valid Colors are -- R Y B G O P")
color_array=["R","Y","B","G","O","P"]
print("")
total_oprtunity=10
print(f"Your Opportunity is begin with {total_oprtunity}")

attempt=0
print("")

def guess_func():
    global color_array
    global attempt

    guess_chance=True
    txt_guess=[]
    random_before_arr=[]
    for _ in color_array:
        random_before_arr.append(random.choice(color_array))

    while guess_chance:
        correct_posi=0
        wrong_posi=0
        if total_oprtunity<11 and total_oprtunity>=1:
            get_guess= input("Guess the Color: ").upper()
            txt_guess=" ".join(get_guess).split(" ")
            print(txt_guess)
            for text in txt_guess:
                if text not in color_array:
                    print("You Input is Not Valid Try Again")
                    continue
            random_arr=random_before_arr[0:len(txt_guess)]
            print(random_arr)
            if txt_guess==random_arr:
                print(f"You Got a Perfect Guess at {attempt}th attempt")
                guess_chance=False
            else:
                attempt+=1
                for index,word in enumerate(random_arr):
                    if word in txt_guess and txt_guess[index]==word:
                        correct_posi+=1
                    elif word in txt_guess and txt_guess[index]!=word:
                        wrong_posi+=1
                print(f"Correct Find: {correct_posi} || Wrong Find: {wrong_posi}")
        else:
            print("You Have 0 attemps to continue")       
guess_func()
