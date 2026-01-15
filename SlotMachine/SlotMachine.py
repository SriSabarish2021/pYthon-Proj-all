import random
def sloter():
    print("Welcome to Slot Machine Game".center(50,"-"))
    print("")
    get_initial_amt=int(input("Place Your Initial Amount: "))

    print(f"Your Current Balance is {get_initial_amt}")
    print("")
    choice_arr=['A','B','C']
    
    correct_val=''
    earned_amt=0
    correct_line=0
    def slot_game():
        get_into_game=input("Press Enter to get into game(n-EXIST): ").lower().strip()
        if get_into_game=='n':
            print("Thanks For Playing")
        def line_bidder():
            nonlocal choice_arr
            result=[]
            nonlocal earned_amt
            nonlocal correct_val
            nonlocal get_initial_amt
            try:
                get_line_bid=int(input("Enter no.of.line to Bid(1-3): "))
                if get_line_bid>3 or get_line_bid<1:
                    print("Please Enter Valid Number")
                    return line_bidder()
                get_line_bid_amt=int(input("Enter AMT to Bid on Each Line: "))
                print(f"Your Bid Per Line is ${get_line_bid_amt}")
                total_bid_all_line=get_line_bid_amt*get_line_bid
                print(f"Your Total Bid is {total_bid_all_line}")
                if get_initial_amt-total_bid_all_line<0:
                    print("Your Balnce is less than or equal to 0")
                    play_again=input("Want to play Again(y/n): ").lower().strip()
                    if play_again=='y':
                        return sloter()
                    else:
                        print("Thank You For Playing")

                
                
                for _ in range(1,get_line_bid+1):
                    random_Resul=[]
                    for _ in range(1,len(choice_arr)+1):
                        random_alpha=random.choice(choice_arr)
                        random_Resul.append(f"{random_alpha}")
                    result.append(random_Resul)
                print(result)
                for val in result:
                    print("")
                    for item in val:
                        print(f"{item} | ",end="")
                print("")       
                for find in result:
                    if find ==['A','A','A'] or find ==['B','B','B'] or find ==['C','C','C']:
                        earned_amt+=5
                
                get_initial_amt=get_initial_amt-total_bid_all_line
                print("")
                print(f"Your Losed AMT is {get_initial_amt}")
                print("")
                get_initial_amt+=earned_amt
                print(f"Your Earned Amount is {earned_amt}")
                print("")
                print(f"Your Total Amount is {get_initial_amt}")

                play_again_after=input("want to play again(y/n)")
                if play_again_after=='y':
                    return line_bidder()
                else:
                    print("Thank You")

                        
                

            except:
                print("Please Enter Valid Number--")
                return line_bidder()
        line_bidder()


    slot_game()
sloter()