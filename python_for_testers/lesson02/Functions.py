# Functions
def reverseStr(str):
    for letter in range(len(str) - 1, -1, -1):
        print(str[letter], end='')


def max(a, b, c):
    if (a > b and a > c):
        return a
    if (b > a and b > c):
        return b
    if (c > a and c > b):
        return c
    return a


def removeDuplicated(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def factorial(number):
    total = 1
    while (number > 0):
        total = (number * total)
        number -= 1
    return total


# Ex1
print("Ex1:")
reverseStr("1234abcd")
print()
print("Ex2:")
print(max(7, 7, -8))
print("Ex3:")
print(removeDuplicated(["1", "2", "3", "3", "3", "3", "4", "5", "5"]))
print("Ex4:")
print(factorial(5))
