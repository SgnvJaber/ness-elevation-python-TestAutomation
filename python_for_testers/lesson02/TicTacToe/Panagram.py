# Function to check whether a string is a pangram or not
# Pangrams are words or sentences containing every letter of the alphabet at least once
def is_pangram(line):
    #All the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #Conveting line_chars to lower case
    line_chars = line.lower()
    for char in alphabet:
        if char not in line_chars:
            print(char)
            return False
    return True

string = 'the quick brown fox jumps over the lazy dog'
print("Pangram:", is_pangram(string))
