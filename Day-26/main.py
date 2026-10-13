# import pandas
# is_on = True
# while is_on:
#     word = input("Enter a word: ").upper()
#     if word == "STOP":
#         is_on = False
#     data = pandas.read_csv("nato_phonetic_alphabet.csv")
#     phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#     output_list = [phonetic_dict[letter] for letter in word]
#     print(output_list)


#####################################################################################################

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)



word = input("Enter a word: ").upper()
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("only letters in alphabet, You dumdass!")
else:
    print(output_list)