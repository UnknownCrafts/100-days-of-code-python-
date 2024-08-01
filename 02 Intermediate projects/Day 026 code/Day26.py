# Converting words so that they are pronouncable using the NATO alphabet

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics = {row.letter:row.code for (index, row) in df.iterrows()}


word = input("Enter a word: ").upper()

print([phonetics[letter] for letter in word])
