#  Emoji Guesser Game  

A fun little Python console game where you try to guess the correct emoji based on hints.  

## 🚀 How to Play
1. The game will randomly pick an emoji from a small set.  
2. You will see a list of possible emojis (`😂 😭 😘 😡`).  
3. Enter the emoji you think is correct.  
4. If your guess is wrong, you’ll get a hint!  
5. Keep guessing until you find the right one 🎉.  

## 📂 Code
```python
from colorama import Fore, Style
import random

print(Fore.LIGHTGREEN_EX + "Welcome to the Emoji Guessing Game! 😊🤣😉" + Style.RESET_ALL)

emoji_dict = {
    "😂": "You use me when you are happy/laughing",
    "😭": "You use me when you are sad/crying",
    "😘": "You use me when you want to kiss someone",
    "😡": "You use me when you are angry"
}

choice = random.choice(list(emoji_dict.keys()))

print(Fore.GREEN + "Guess the emoji: " + Style.RESET_ALL)
print("😂", "😭", "😘", "😡", sep=" . ")

while True:
    guess = input("Enter the emoji you guessed: ")

    if guess == choice:
        print(Fore.LIGHTBLUE_EX + "🎉 Congratulations! You guessed it right!" + Style.RESET_ALL)
        break
    else:
        print("❌ Sorry! Wrong guess\n👉 Here is your hint:")
        print(emoji_dict[choice])
        print(Fore.RED + "Try again!" + Style.RESET_ALL)
```

## 🛠 Requirements
- Python 3.x  
- Install colorama → `pip install colorama`  

## 🎯 Example Gameplay
```
Welcome to the Emoji Guessing Game! 😊🤣😉
Guess the emoji: 
😂 . 😭 . 😘 . 😡
Enter the emoji you guessed 😭
❌ Sorry! Wrong guess
👉 Here is your hint:
You use me when you are happy/laughing
Try again!
```
output:
<img width="1532" height="214" alt="Screenshot 2025-08-20 214551" src="https://github.com/user-attachments/assets/4a72bfa2-017e-43e1-b38b-e13c6ce33a7e" />



## Modifications to try:
- Add more emojis 
- Play multiple rounds with score tracking  
- Shuffle the emoji options each round  
- Let players quit anytime with `quit`  
