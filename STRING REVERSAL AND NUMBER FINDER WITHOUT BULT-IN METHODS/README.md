# String Reversal & Number Finder

A simple Python script that:
1. Reverses a given string.
2. Finds the smallest number in a list.
3. Finds the greatest number in a list.
   Here I didnt use any built in functions like min() or max()

## Features
- **Reverse Function**: Takes a string and returns it in reverse order.
- **Smallest Function**: Iterates through a list of numbers to find the smallest value.
- **Greatest Function**: Iterates through a list of numbers to find the largest value.

## Usage
```python
def reverse(strings):
    rev = ""
    for i in range(len(strings)-1, -1, -1):
        rev += strings[i]
    return rev

def smallest(numbers):
    smallest_number = numbers[0]
    for i in numbers:
        if smallest_number > i:
            smallest_number = i
    return smallest_number     

def greatest(numbers):
    greatest_number = numbers[0]
    for i in numbers:
        if greatest_number < i:
            greatest_number = i
    return greatest_number     

# Example usage
print(reverse("python"))  # Output: nohtyp
numbers = [2, 8, 9, 1]
print(smallest(numbers))  # Output: 1
print(greatest(numbers))  # Output: 9
```



## Output
```
nohtyp
1
9
```

## 
