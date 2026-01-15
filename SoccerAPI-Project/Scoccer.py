import requests
from pprint import pprint
import random

print("Welcome to Soccer Game View Point")
print("")
API_url="https://api.football-data.org/v4/competitions/"




def Data_Showing(all_data):
    get_array=all_data["competitions"]
    
    get_team_name=map(lambda data:data["name"],get_array)
    
    tournament_list=list(get_team_name)[0:10]
    shulffle_arr=random.shuffle(tournament_list)
    
    for index,tournament in enumerate(tournament_list):
        print(f"{index+1}:{tournament}")

    print("")
    def get_user_inp():
        try:
            get_inp_tour=int(input("From The Tournament Enter Which Tourn Details You Want(1-10): "))
            print("")
            print(f"You Has Been Selected--{tournament_list[get_inp_tour-1]}")
            print("")
            print("Lets I Show you the Details to Watch out:")
            get_tournament=filter(lambda data:data["name"]==f"{tournament_list[get_inp_tour-1]}",get_array)
            list_of_tournament=list(get_tournament)   
            print("")  
            print("Here it is the Current Seasons Details:".center(80,'-'))
            for key,match_data in list_of_tournament[0]["currentSeason"].items():
                print(f"{key}: {match_data}")

        except:
            print("")
            print("Enter Proper Value as Input")
            return get_user_inp()
    get_user_inp()
    

def fetchin_data(url):

    try:

        get_data=requests.get(url).json()
        print(requests.get(url))
        # pprint(get_data)
        Data_Showing(get_data)
    except:
        print("There is a Error in Server Please Visit Later....")


fetchin_data(API_url)

