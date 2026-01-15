import string
import random
# print(list(string.ascii_lowercase))

print("Welcome to Random Password Generation App")
print("")

while True:
    get_password_len=input("Enter the Password Lenght you want(5-10): ")
    if get_password_len.isdigit() and int(get_password_len)<11 and int(get_password_len)>=5:
        ran_char_one=list(string.hexdigits)
        password=random.shuffle(ran_char_one)      
        user_password="".join(ran_char_one[0:int(get_password_len)])
        print(f"Your Password is = {user_password}")
        break
    else:
        print("mo")
        break

