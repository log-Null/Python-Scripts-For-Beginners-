def prime(number):
    if number <=1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def max_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

def vowel(word):
    words=[i for i in word if i in 'aeiouAEIOU']
    return len(words)
prime_number=int(input("Enter a number to check if it is prime: "))
print(prime(prime_number))
maximum=int(input("Enter three numbers to find the maximum: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(max_number(num1,num2,num3))
vowels = input("Enter a sentence to count vowels: ")
print(vowel(vowels))
