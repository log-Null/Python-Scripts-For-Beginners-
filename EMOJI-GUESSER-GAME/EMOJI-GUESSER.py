#EMOJI GUESSER GAME
from colorama import Fore, Style
import random
print(Fore.LIGHTGREEN_EX+"Welcome to the Emoji Guessing Game! 😊🤣😉"+Style.RESET_ALL)
dict={"😂":" you use me when you are happy",
      "😭":" you use me when you are sad",
      "😘":" you use me when you are want to kiss someone",
      "😡":" you use me when you are angry"
     }
choice=random.choice(list(dict.keys()))
print(Fore.GREEN + "Guess the emoji: " + Style.RESET_ALL )
print( "😂","😭","😘","😡", sep=".")
while True:
    guess=input("Enter the emoji you guessed")
    if guess == choice:
        print(Fore.LIGHTBLUE_EX + "Congratulations! You guessed it right!" + Style.RESET_ALL)
        break
    else:
        print("sorry! Wrong guess\nHere is your hint:")
        print(dict[choice])
        print(Fore.RED + "Try again!" + Style.RESET_ALL)
