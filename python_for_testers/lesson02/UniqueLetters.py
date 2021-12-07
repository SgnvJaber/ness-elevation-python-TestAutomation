def unique_letters(word):
    unique_word = []
    for letter in word:
        if letter not in unique_word:
            unique_word.append(letter)
    return unique_word


def count_letter_occurrence(word):
    occurrence = {}
    for letter in word:
        if letter in occurrence.keys():
            count = occurrence.get(letter)
            occurrence[letter] = count + 1
        if letter not in occurrence.keys():
            occurrence[letter] = 1
    return occurrence


print(unique_letters("hello"))
print(count_letter_occurrence("Hello World"))
