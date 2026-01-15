from cryptography.fernet import Fernet 

print("Welcome to our New Product".center(50,'-'))

set_master_pass=input("Set up you Account With Master Password: ")
print("Thank You for Creating Master Pass Remember While Returning")
key=''
def random_key():
    global key
    key=Fernet.generate_key()
    print(type(key))
random_key()
def build_locker(password):
    lock_key=Fernet(key)
    encode_key=lock_key.encrypt(password.encode())
    return(encode_key)


def view_pass(lock_id):
    unlock_key=Fernet(key)
    decode_key=unlock_key.decrypt(lock_id).decode()
    return(decode_key)

def password_func(set_master_pass):
    global build_locker
    global view_pass
    get_master_pass=input("Enter Master Password: ")
    if set_master_pass==get_master_pass:
        print("Create Your ACC".center(30,'*'))
        acc_creation=input("User-Name: ")
        acc_pass=input("Pass: ")
        print("")
        print("Account Created Succesfully")
        decoder=build_locker(acc_pass)
        print("")
        print(f"Your Decode Key Is---:\n{str(decoder)[2:-1]}")
        pass_access=input("Want To View Pass or Exist (y/x):").strip().lower()
        print(f"youpass={(len(acc_pass)+5)*'*'}")
        to_view=input("To View Password Enter (V/E):").lower().strip()
        if to_view=='v':
            get_decode_id=input("Enter Decode Id: ")
            decoded_password=view_pass(get_decode_id)
            print(decoded_password)
        elif pass_access=='e':
            print("Thank You")
    else:
        print("You Have Entered Wrong Master Password") 
        return password_func(set_master_pass)  
password_func(set_master_pass)