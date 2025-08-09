# -----------------------------
# 🎯 Game: Heads or Tails 🪙
# -----------------------------
import random

# 💠 ASCII Art for the coin
print("""
   *************
  *   HEADS    *
   *************
       ||||
       ||||
   *************
  *   TAILS    *
   *************
""")

print("""
🎉 Welcome back to our game!
🪙 Choose a method to flip the coin:
1️⃣  Using random.random()
2️⃣  Using random.randint()
""")

user_Choice = input("Enter your choice (1 or 2): ")
user_guess = input("Enter your guess (heads or tails): ").lower()

if user_Choice == "1":
    my_random = random.random()
    if my_random >= 0.5:
        my_random = "heads"
        if my_random == user_guess:
            print(f"🏆 You win! 🎯\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
        else:
            print(f"❌ You lost 💔\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
    else:
        my_random = "tails"
        if my_random == user_guess:
            print(f"🏆 You win! 🎯\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
        else:
            print(f"❌ You lost 💔\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")

elif user_Choice == "2":
    my_random = random.randint(0, 1)
    if my_random == 0:
        my_random = "heads"
        if my_random == user_guess:
            print(f"🏆 You win! 🎯\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
        else:
            print(f"❌ You lost 💔\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
    else:
        my_random = "tails"
        if my_random == user_guess:
            print(f"🏆 You win! 🎯\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")
        else:
            print(f"❌ You lost 💔\n🪙 I chose [{my_random}]\n🙋 You chose [{user_guess}]")

else:
    print(f"⚠️ Invalid input: {user_Choice} ❗ Please choose 1️⃣ or 2️⃣")
# -----------------------
# Game Over ⚠️ 
# -----------------------