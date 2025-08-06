# show welcome message with pirate ascii code 
# tell user there are two doors !
print("""
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
Welcome to my island
There are two doors in front of you. 🟥 a red door and 🟦 a blue door
""")
# which door the user chose it ?
# use .lower() to small charcters
wich_door = input ("""which door do you want to open! 
just write: red door
or write: blue door
""").lower()
# use if condition to take user answer
if wich_door ==  "blue door":
    print(" you opened a blue 🟦 door!")
    print("Oops, You chose the crocodile door\nGame over🐊🐊🐊🐊")

elif wich_door == "red door":
    print("Greet!, You opened a red 🟥 door!\nand you entered a room")
    print("You found three boxes: ⬜White, ⬛Black, 🟩Green")
    # ask user wich box he is open!
    which_box = input ("Which Box do you open? ").lower()
    # use if condition to take user answer
    if which_box == "white":
        print("""
        Oops!, you oppened a box filled with snakes🐍🐍🐍
        Game Over☠️☠️☠️🏴‍☠️
        """)
    elif which_box == "black":
        print("""
        Oops!, you oppened a box filled with spiders🕷️🕷️🕷️
        Game Over☠️☠️☠️🏴‍☠️
        """)
    elif which_box == "green":
        print("""
        Congratulation!😃, You found the treasure 🥇🥇🥇
        """)
    # chek if the user write any input wrong!
    else:
        print(f"Your input [{which_box}]isn't defined\nGame Over🦧🦧🦧")  
 
# chek if the user write any input wrong!
else:
    print(f"Your input [{wich_door}] isn't defined\nGame Over🦧🦧🦧")
#-----------------------
# Game Over
#-----------------------