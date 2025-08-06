# -----------------------------
# Gamee Heads or Tails 
# -----------------------------
import random
print("""
      Welcome back to our Game 
      Choose a method to toss the coin
      1- Using random.random()
      2- Using random.randint()
      """)
user_Choice = input("Enter your choice (1 or 2): ")
user_guess = input("Enter your guess (Heads or Tails): ").lower()
if user_Choice =="1":
    my_random = random.random()
    if my_random >= 0.5:
        my_random = "heads"
        if my_random == user_guess:
            print(f"You win\nI Choose[{my_random}]\nAnd you Choose[{user_guess}]")
        else:
            print(f"You Lost\nI Choose[{my_random}]\nAnd you choose[{user_guess}]")
    else:
        my_random ="tails"
        if my_random == user_guess:
            print(f"You win\nI Choose[{my_random}]\nAnd you Choose[{user_guess}]")
        else:
            print(f"You Lost\nI Choose[{my_random}]\nAnd you choose[{user_guess}]")
elif user_Choice =="2":
    my_random = random.randint(0,1)
    if my_random == 0:
        my_random = "heads"
        if my_random == user_guess:
            print(f"You win\nI Choose[{my_random}]\nAnd you Choose[{user_guess}]")
        else:
            print(f"You Lost\nI Choose[{my_random}]\nAnd you choose[{user_guess}]")
    else:
        my_random = "tails"
        if my_random == user_guess:
            print(f"You win\nI Choose[{my_random}]\nAnd you Choose[{user_guess}]")
        else:
            print(f"You Lost\nI Choose[{my_random}]\nAnd you choose[{user_guess}]")
else:
    print(f"Invaild input: {user_Choice} just choose 1 or 2")
