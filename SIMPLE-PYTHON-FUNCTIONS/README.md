# 🐍 Python Basics: Prime Check, Max Number, and Vowel Counter

This mini Python script includes three beginner-friendly Python functions:

1. `prime(number)` – Checks if a number is prime.
2. `max_number(num1, num2, num3)` – Returns the largest of three numbers.
3. `vowel(word)` – Counts the number of vowels in a string.

---

## ✅ Code:

```python
# Function to check if a number is prime
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to find the maximum of three numbers
def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# Function to count the number of vowels in a string
def vowel(word):
    words = [i for i in word if i in 'aeiouAEIOU']
    return len(words)

# Sample Outputs
print(prime(3))                          # ➝ True
print(max_number(12, 3, 6))              # ➝ 12
print(vowel("Python is a coding language"))  # ➝ 8
```

---

## 🔍 Function Details:

### 1. `prime(number)`
- Returns `True` if the number is prime, else `False`.
- Skips all numbers less than or equal to 1.
- Efficiently checks up to the square root of the number.

**Example:**
```python
prime(3) ➝ True
prime(10) ➝ False
```

---

### 2. `max_number(num1, num2, num3)`
- Compares all three numbers and returns the largest one.

**Example:**
```python
max_number(12, 3, 6) ➝ 12
```

---

### 3. `vowel(word)`
- Counts the total number of vowels in the given string.
- Both lowercase and uppercase vowels are considered.

**Example:**
```python
vowel("Python is a coding language") ➝ 8
```

---

## 🚀 How to Run

Save this script in a file like `basics.py`, then run:

```bash
python basics.py
```

---

## 📘 Tips

- Use `return` in functions instead of `print()` for better reusability.
- Try modifying these functions to handle lists or user input.
- This is a great base for your first Python projects!

---
