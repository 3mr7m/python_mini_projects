askuser = int(input("How old are you? "))
print(f"You was born in {(2025 - askuser)}")
#############################################################
askuser = int(input("Enter num of minuties: "))
hour = askuser // 3600
min = (askuser % 3600) // 60
sec = askuser % 60
print(f"Your tak {hour}h and {min}m and {sec}s")
#############################################################
lenght = float(input("Enter the lenght: "))
widght = float(input("Enter the widght: "))
pricemeter = float(input("How much price for one meter: "))
totalarea = lenght * widght
print(f"Your total area is: {(totalarea)}m")
print(f"Your total price is: ${totalarea * pricemeter}")
#############################################################
user_input = input("Enter two digits: ")
user1 = user_input [0]
user2 = user_input [1]
print (int(user1) + int(user2))
