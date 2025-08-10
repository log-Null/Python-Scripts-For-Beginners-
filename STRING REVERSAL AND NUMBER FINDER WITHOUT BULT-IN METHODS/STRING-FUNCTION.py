def reverse(strings):
    rev=""
    for i in range(len(strings)-1,-1,-1):
         rev+=strings[i]
    return rev
def smallest(numbers):
    smallest_number= numbers[0]
    for i in numbers:
        if smallest_number>i:
            smallest_number=i
    return smallest_number     
def greatest(numbers):
    greatest_number= numbers[0]
    for i in numbers:
        if greatest_number<i:
            greatest_number=i
    return greatest_number     

print(reverse("python"))
numbers = [2, 8, 9, 1]
print(smallest(numbers))
print(greatest(numbers))
