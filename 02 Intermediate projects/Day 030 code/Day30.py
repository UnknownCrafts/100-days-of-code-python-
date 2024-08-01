# Converting words so that they are pronouncable using the NATO alphabet now with error handling

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics = {row.letter:row.code for (index, row) in df.iterrows()}

word = ""
phonestics_list = []
def user_input():
    global word, phonestics_list
    word = word = input("Enter a word: ").upper()
    try:
        phonestics_list = [phonetics[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
        return False
    return True

while user_input() == False:
    pass

print(phonestics_list)
