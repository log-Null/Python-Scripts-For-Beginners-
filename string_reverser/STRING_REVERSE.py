def reverse(string): 
    reversed_string=string[::-1]
    return reversed_string
if __name__ == "__main__":
    string=input("enter a string")
    print(reverse(string))
