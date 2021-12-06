### Strings  ###
first_name = "Saed"
last_name = "Jaber"
age = 25
age_str = str(age)
line = "Python is a general purpose computer programming language"
words = "Hello world"
print(first_name.upper())
print(last_name.lower())
print(first_name[1:])
print(last_name[:len(last_name) - 1])
print(line.count("computer"))
print(line.find("computer"))
print(line.replace(" ", ""))
seperate_line_index = words.find(" ")
print(words.split(" ")[1])
# Other option:
print(words[seperate_line_index + 1:])
### List  ###
my_list = ["Country1", "Country5", "Country3", "Country2", 'Country4']
print(my_list[:3])
country = my_list[0]
my_list[0] = my_list[1]
my_list[1] = country
print(my_list)
my_list.reverse()
print(my_list)
my_list.reverse()
my_list.reverse()
my_list.sort()
print(my_list)
my_list.pop(len(my_list) - 1)
print(my_list)
my_list.remove(my_list[len(my_list) - 1])
print(my_list)
my_list.insert(int(len(my_list) / 2), "NewCountry")
print(my_list)
### Dictionary  ###
phone_book = {"saed": "0525664962", "kuku": "0534339531", "kuku2": "0525339482"}
print(phone_book)
print(len(phone_book))
phone_book["kuku3"] = "0524553951"
print(phone_book)
phone_book.update({'kuku4': '0525449385'})
print(phone_book)
