# Ex1
def print_message(argument):
    try:
        print("Ok " + argument + " ", end='')
        print("argument is valid")
    except Exception as e:
        print("argument is not valid fixing it-", end='')
        print("Ok " + str(argument))
        print("some error occured,see details:", e)


print("Ex1:")
print_message("Hello")
print_message(3)
print_message(2.5)
print_message(True)
print_message(123)
# Ex2
print("Ex2:")
try:
    my_list = [1, 2, 0]
    my_list[6] = my_list[1] / my_list[2]
    print(my_list)
except IndexError:
    print("Your List's index is out of bound")
except ZeroDivisionError:
    print("You can't divide number by zero")
