# محتاج تعمل رسم بياني علي ورقه وتقعد بكوباية شاي وتكبره علشان يبقا توب
# Welcome message
print("*************** Welcome To Egyptian Site *************")
# Ask The User if he is Egyptian or not?
is_egyptian = input("Are you Egyptian?yes or no: ").lower()
# Use if condition to filtter The user answer
if is_egyptian == "yes":
    print("This is first step!")
    # Ask User About His age ?
    age = int(input ("How old are you? "))
    # Use if condition to filtter user age 
    if age >= 18:
        print("You can make ID")
        # Ask user about his name ?
        user_name = input("What is your full name? ")
        # Welcome message again
        print(f"Hi, {user_name} Long live Egypt😁")
        # Print user data to user
        print(f"""Ok!, Here is your data:\n
              You Are Egyptian\n
              You was born in {2025-age}\n
              You aready have {age}\n
              You're full name is {user_name}\n
              You're Single\n
              """)
    elif age < 18:
        print ("You can't make ID wait until 18")
    else:
        print(f"Your input {age} understood")
elif is_egyptian == "no":
    print("Sorry you can't use this web!")
    print("You can use this websit if you're Egyptian")
else:
    print(f"Your input {is_egyptian} understood")
