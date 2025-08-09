# Show welcome message with pirate ASCII art
# Tell the user there are two doors
print("""
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
Welcome to my island!
There are two doors in front of you: 🟥 a red door and 🟦 a blue door.
""")

# Ask which door the user chooses
# Use .lower() to convert to lowercase
which_door = input("""
Which door do you want to open?
Just type: red door
Or type: blue door
""").lower()

# Use if condition to take user’s answer
if which_door == "blue door":
    print("You opened the 🟦 blue door!")
    print("Oops! You chose the crocodile door.\nGame over 🐊🐊🐊🐊")

elif which_door == "red door":
    print("Great! You opened the 🟥 red door!\nAnd you entered a room.")
    print("You found three boxes: ⬜ White, ⬛ Black, 🟩 Green")
    
    # Ask which box the user opens
    which_box = input("Which box do you open? ").lower()
    
    # Use if condition to take user’s answer
    if which_box == "white":
        print("""
        Oops! You opened a box filled with snakes 🐍🐍🐍
        Game Over ☠️☠️☠️🏴‍☠️
        """)
    elif which_box == "black":
        print("""
        Oops! You opened a box filled with spiders 🕷️🕷️🕷️
        Game Over ☠️☠️☠️🏴‍☠️
        """)
    elif which_box == "green":
        print("""
        Congratulations! 😃 You found the treasure 🥇🥇🥇
        """)
    # Check if the user entered an invalid input
    else:
        print(f"Your input [{which_box}] isn't valid.\nGame Over 🦧🦧🦧")  

# Check if the user entered an invalid input
else:
    print(f"Your input [{which_door}] isn't valid.\nGame Over 🦧🦧🦧")

# -----------------------
# Game Over
# -----------------------
