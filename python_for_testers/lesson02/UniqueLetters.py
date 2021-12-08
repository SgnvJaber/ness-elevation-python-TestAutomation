# Ex1
def unique_letters(word):
    unique_word = []
    for letter in word:
        if letter not in unique_word:
            unique_word.append(letter)
    return unique_word


# Ex2
def count_letter_occurrence(word):
    occurrence = {}
    temp = word.replace(" ", "").upper()
    for letter in temp:
        if letter in occurrence.keys():
            count = occurrence.get(letter)
            occurrence[letter] = count + 1
        if letter not in occurrence.keys():
            occurrence[letter] = 1
    # Source:https://www.geeksforgeeks.org/python-reverse-dictionary-keys-order/
    # dic_occurrence=dict(sorted(occurrence.items(), key=lambda item: item[1],reverse=True))
    dic_occurrence = dict(reversed(list(occurrence.items())))
    return dic_occurrence


print("Ex1:")
print(unique_letters("hello"))
print("Ex2:")
my_dict = count_letter_occurrence("Hello World")
for x in my_dict:
    print(x + ":" + str(my_dict[x]))
