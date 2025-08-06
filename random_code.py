# -----------------------------------
# This file for test code of octucode
# -----------------------------------
# hoe to use random and chose num random
# first import module random
# import random
# make variable to do random (my random)
# use (module random) with variable (.randint()) 
# my_random = random.randint(-5,5)
# print variable that i made 
# print(my_random)
# ------------------------------------------------
import random
pin_user = int(input("Enter a 4-digit PIN code: "))
pin_random = random.randint(1000,9999)
if len(str(pin_user))!=4:
    print("please Enter 4-digit")
elif len(str(pin_user))==4:
    if pin_user == pin_random:
        print(f"Greet choise:\nYour PIN: {pin_user}\nmy PIN: {pin_random}")
    elif pin_user != pin_random:
        print(f"Wrong password:\nYour PIN: {pin_user}\nMy PIN: {pin_random}")
# -------------------------------------------
# you can use if condition without use (else)
# -------------------------------------------
