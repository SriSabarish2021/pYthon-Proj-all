import requests

print("Welcome to Currency Convertor App".center(50,"-"))
print("")
get_amt=int(input("Enter the Amount to Convert: "))
print("")
get_from_curr=input("Enter the County Code of parent Currency: ")
print("")
get_to_curr=input("Enter Change Currency: ")
print("")

URL=f"https://v6.exchangerate-api.com/v6/b4be06c6e42246cc91f78147/latest/{get_from_curr}"

def get_data(url,to_curr,amt):
    data=url
    get_data=requests.get(data).json()["conversion_rates"][f"{to_curr}"]
    total_conversion=f"Your Total Conversion is: {int(get_data)*int(amt)}"
    print(total_conversion)
    
get_data(URL,get_to_curr,get_amt)
