# Ex1
print("EX1:")
x = 0.5
y = 0.2
if (x > y):
    print("x is greater than y")
elif (y > x):
    print("y is greater than x")
else:
    print("The sum of x and y is: ", (x + y))
# Ex2
print("EX2:")
numbers = [8, 5, 9]
if (numbers[0] > numbers[1]):
    print("First One is Bigger")
elif (numbers[1] > numbers[0]):
    print("Second One is Bigger")
else:
    print("Both are Equal")
# Ex3
print("Ex3:")
print("For Loop:1-10")
for x in range(10):
    print(x + 1)
print("While Loop:1-10")
num = 0
while (num < 10):
    print(num + 1)
    num += 1
print("Pair Numbers:30-50")
for x in range(30, 51):
    if (x % 2 == 0):
        print(x)
print("Non Pair Numbers:20-40")
for x in range(20, 41):
    if not (x % 2 == 0):
        print(x)
# Ex4
print("Ex4:")
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
# a
for country in countries:
    print(country + " ", end='')
# b
print()
for country in countries:
    if (country == "Israel"):
        print(country)
# C
if (countries[2] == "China"):
    print("Yes,it is there")
else:
    print("No Sorry...")
# D
print("First index Length: ", len(countries[0]))
# Ex5(Do with match case)
print("Ex5:")
value = 120
match value:
    case value if value > 0 and value <= 6:
        print("Go to Kindergarten")
    case value if value >= 7 and value <= 18:
        print("Go to School")
    case value if value >= 19 and value <= 67:
        print("Go to Work")
    case value if value >= 68 and value <= 120:
        print("Collecting Pension")
# Ex6
print("Ex6:")
job = "QA"
if (job == "QA"):
    print("15000")
elif (job == "Bank Teller"):
    print("10,000")
elif (job == "Teacher"):
    print("5000")
elif (job == "Average Salary"):
    print("9100")
else:
    print("No info on the given job")
# Ex7
print("Ex7:")
names = {"Yoni": "12345", "Moshe": "45678", "David": "54321"}
for id in names.values():
    print("ID:", id)
for name in names.keys():
    print("Name:", name)
# Ex8
print("Ex8:")
set_numbers = {1, 2, 3, 4, 5, 30, 15, 45, 60}
for number in set_numbers:
    if (number % 3 == 0 and number % 5 == 0):
        print("Number:", number)
# Ex9
print("Ex9:")
letters = ['o', 'l', 'l', 'e', 'h']
word = ""
for i in range(len(letters) - 1, -1, -1):
    word += letters[i]
print(word)
# Ex10
print("Ex10:")
numbers = [15, 2, 36, 20, 7]
if (numbers[0] > numbers[1]):
    if (numbers[1] > numbers[2]):
        print("First Number:", numbers[0])
    else:
        print("Third Number:", numbers[2])
else:
    if (numbers[1] > numbers[2]):
        print("Second Number:", numbers[1])
    else:
        print("Third Number:", numbers[2])
max = numbers[0]
sum = 0;
for number in numbers:
    sum += number
    if (number > max):
        max = number
print("Max:", max)
print("Sum:", sum)

# Ex11
print("Ex11:")
number = 8
# Rowan's idea to minimize iteration
divider = number / 2
isPrime = True
for x in range(2, int(divider)):
    if (number % x) == 0:
        isPrime = False
        break

if isPrime:
    print("Prime Number")
else:
    print("Not a Prime Number")
