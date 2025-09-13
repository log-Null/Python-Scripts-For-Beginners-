# Message Automator App 🖥️💬

## Overview
**Message Automator App** is a Python-based automation tool designed to type **predefined messages automatically** in any active text input field. While simple in functionality, it demonstrates the power of **Python automation with PyAutoGUI** and can be used for:

- Fun demonstrations or reels  
- Learning automation scripting  
- Experimenting with automated typing in text editors  

> ⚠ **Disclaimer:** This project is intended for **educational and demonstration purposes only**. Do **not** use it to spam, annoy, or send messages on live platforms without consent.

---

## Features
- Automated typing of **custom, pre-defined messages**.
- Console logging of **timestamps** for each message sent.
- Configurable **time intervals** between messages.
- Lightweight, dependency-minimal, and **easy to run**.
- Demonstrates practical use of **Python scripting for automation**.

---

## Predefined Messages
The default script types messages in a **loop** such as:

- "Peek-a-boo! I see you 👁️"  
- "Hello… is it me you’re looking for?"  
- "Oops… did I pop up again?"  
- "Back. Again. You’re welcome"  
- "Yes, yes… I know you missed me 😏"

You can **edit the script** to add, remove, or modify messages as needed.
<img width="1817" height="996" alt="Screenshot 2025-09-13 135743" src="https://github.com/user-attachments/assets/086838b8-b711-4216-b41c-afda8d78e2cb" />


---

## requirements

1. Ensure you have **Python 3.x** installed on your system.
2. Install the required package:

```
pip install pyautogui
```


## Usage Instructions

1. Open any text editor or input field where you want the messages to appear (e.g., Notepad, VS Code).  
2. Make sure the **text input area is active**.  
3. Run the script
4. The script will wait **2 seconds** before starting to give you time to focus on the desired window.  
5. Watch as your predefined messages appear automatically.  

> Tip: The script prints **timestamps** in the console each time a message is typed, which is useful for logging and demonstration purposes.

---

## Customization

- **Change Messages:** Edit the `pyautogui.typewrite()` lines to add your own messages.
- **Adjust Typing Interval:** Modify `time.sleep(5)` to make the bot type faster or slower.
- **Loop Control:** Currently, the script loops indefinitely (or until manually stopped). You can adjust the loop or add a termination condition.

---

## Safety Tips

- **Emergency Stop:** Move your mouse cursor to the **top-left corner** of the screen to trigger PyAutoGUI’s fail-safe.  
- **Do not use on live chat platforms** unless you have explicit consent.  
- **Record safely:** Ideal for reels, demos, or local experiments only.

---

## Example Console Output

```
2025-09-13 12:45:10.123456
2025-09-13 12:45:15.123456
2025-09-13 12:45:20.123456
...
```

This shows the **exact timestamp** for each message sent.

---

## Learning Objectives
This project is a great starting point for:

- Understanding **Python automation libraries** like PyAutoGUI.
- Practicing **loops, delays, and console logging**.
- Creating **reel-ready demonstration projects** using code.

---

## Future Enhancements
- Add **randomized message order** for variety.  
- Integrate **typing animations** or **sound effects**.  
- Support **multi-window typing** or **custom GUI interfaces**.  
- Include a **GUI to add messages dynamically** instead of editing the script manually.

---

## License
This project is licensed under the **MIT License** – free to use for **personal, educational, and demonstration purposes**.

---

## Acknowledgements
- [Spam bot using PyAutoGUI](https://www.geeksforgeeks.org/python/spam-bot-using-pyautogui/) – for enabling Python automation.  
- CODEDEX– for excellent resources and tutorials on automation scripting.
