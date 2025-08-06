#------------------------------------
# use ' elif ' in if condition
# use ' else ' in if condition
# use ' > ' in if condition
# use ' < ' in if condition
# use ' == ' in if condition
# use ' != ' in if condition
# use ' or ' in if condition
# use ' and ' in if condition
# use ' .lower() ' in if condition
# use ' .upper() ' in if condition
#------------------------------------
print("****************** Welcome **********************")
degree = float(input("Enter your degree: "))
if degree >= 90:
    print("your degree is: امتياز")
elif degree >= 75:
    print("your degree is: جيد")
elif degree >= 50:
    print("your degree is: مقبول")
elif degree < 50:
    print("your degree is: ضعيف")
else:
    print("False input try again later!")
############################################################
password = "abcd1234"
askuser = input("Enter password: ")
if askuser == password:
    print("Welcome")
else:
    print("Sorry,Wrong input")
############################################################
ask = input ("Enter: yes or no or maybe\n").lower()
if ask == "yes":
    print("You Enterd 'yes'")
elif ask == "no":
    print("You Enterd 'No'")
elif ask == "maybe":
    print("You Enterd 'maybe'")
else:
    print("Try later!")
############################################################
num = 7
usernum = int(input("Gusse num from one to ten: "))
if usernum == num:
    print("Wow, Your greet")
else:
    print("False,try again")
#############################################################
print ("Welcom to our app")
askuser = float(input("Enter the num: "))
if askuser <0:
    print("The num is nigative")
elif askuser >0:
    print("The num is positive")
else:
    print("The num is zero")
#############################################################
area = input("Choose your area: Cairo,Tanta or Alex: ").lower()
if area == "cairo":
    print(f"you choose {area}, Welcome!")
elif area == "tanta":
    print(f"you choose {area}, Welcome!")
elif area == "alex":
    print(f"you choose {area}, Welcome!")
else:
    print(f"The {area} isn't in our list")
#############################################################
age_user = int(input("Enter your age pleese: "))
license_user = input("Do you have a License?'yes' or 'no': ").lower()
if age_user>=18 and license_user=="yes":
    print("yo can drive!")
elif age_user<18 or license_user=="no":
    print("Sorry, you can't drive!")
else:
    print("try later!")
##############################################################
