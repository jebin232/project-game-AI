import pyttsx3
from numpy import random as rp
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("welcome you for starting the game if you are ready let's begin the game")
engine.runAndWait()

def speck(sp):
    engine.say(sp)
    engine.runAndWait()
    engine.stop()

speck("hai to all and how are you ")
value = ["r", "p", "s"]
human_point = 0
computer_point = 0
chance = 5
level = 0
n = str(input("""r for ready
n for no
Enter your option:"""))
if n == "r":
    speck("now we can begin the game")
else:
    speck("Thank you for visiting us")
while n == "r" and level < chance:
    human = input("""
For s= s
For rock= r
For paper= p
Enter your number:""")
    computer = rp.choice(value)
    print(f"you have only {chance - level} chance to finish")
    print("computer guess:", computer)
    level += 1
    if human == computer:
        speck("No point")
    elif human == "s" and computer == "r":
        speck("you got one poin")
        human_point += 1
    elif human == "s" and computer == "p":
        speck("I got one point ")
        computer_point += 1
    elif human == "r" and computer == "s":
        speck("you got one point")
        human_point += 1
    elif human == "r" and computer == "p":
        speck("I got one point")
        computer_point += 1
    elif human == "p" and computer == "s":
        speck("you got one point")
        human_point += 1
    elif human == "p" and computer == "r":
        speck("I got one point")
        computer_point += 1
    else:
        break

print(f"you {human_point} and computer {computer_point}")
if human_point == computer_point:
    speck("Match Draw")
elif human_point > computer_point:
    speck(f"you won by {human_point} points")
else:
    speck(f"I won the game by {computer_point} points")
