# rabbit_game.py
# This is a simple game where a player can place a rabbit on a 3x3 grid of trees.
print("\nWelcome to Our Game!\n")
# Initialize the game board
my_list = [['🌳' , '🌳' , '🌳'],['🌳' , '🌳' , '🌳'],['🌳' , '🌳' , '🌳']]
# Print the current table format
print(f"{my_list[0]}\n{my_list[1]}\n{my_list[2]}")
print("Where Should The Rabbit go? '🐇'")
# Take two numbers from the player
num = input("Please Enter two Number for a row and a coulumn: ")
# Make sure the inputs are two numbers only + an error message if they are not two numbers
if not num.isdigit() or len(num) != 2:
    print(f"Please Enter Right Numbers")
# Make sure the numbers are between 1 and 3 + an error message if they are out of range
elif int(num[0]) < 1 or int(num[0]) > 3 or int(num[1]) < 1 or int(num[1]) > 3:
    print(f"Please Enter Right Numbers Between 1 and 3")
else:
    # Convert row number from human numeral system (1-3) to Python (0-2)
    num_row = int(num[0]) - 1
    # Convert column number from human numeral system to Python
    num_coulmn = int(num[1]) - 1
    # Place the rabbit in the selected place + print the table after modification
    my_list[num_row][num_coulmn] = '🐇'
    print(f"{my_list[0]}\n{my_list[1]}\n{my_list[2]}")
# Game Over$