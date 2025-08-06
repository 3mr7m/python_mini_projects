#--------------------------- Calculator -----------------------
# ------------------------------
# this project need some edit$$$
# ------------------------------
# ask user about the num
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

# ask user what he want to do
ask = input('Chek the list you can use: [+,-,*,//,%]: ')

# if condetion 
# if user want to plus numbers
if ask == "+":
    print (f'Here is your result: {num1+num2}')

# if user want to minus numbers
elif ask=="-":
    print (f'Here is your result: {num1-num2}')

# if user want to multiplication numbers
elif ask=="*":
    print (f'Here is your result: {num1*num2}')

# if user want to division numbers
elif ask=="//":
    print (f'Here is your result: {num1//num2}')

# if user want the rest of the section numbers
elif ask=="%":
    print (f'Here is your result: {num1%num2}')

# if user input false 
else:
    print(f'your input [{ask}] is false trye again')
