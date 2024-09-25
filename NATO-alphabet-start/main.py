# TODO 1. create a dict in this format:
# {"A": "Alfa", "B", Bravo}

# TODO 2. The user writes text and each letter is translated into a phonetic alphabet:
# Thomas
# ['Tango', 'Hotel', 'Oscar']

# Working with pands
import pandas

# step one: create a dict from the CSV
df = pandas.read_csv('nato_phonetic_alphabet.csv')
#print(df)
index_phonetic_alphabet = df.set_index('letter')['code'].to_dict()
#print(index_phonetic_alphabet)

# index_phonetic_alphabet_com = {key: value for (key, value) in df.items()}
# print(index_phonetic_alphabet_com)
name = input("Enter the name you need in your alphabet: ")
#name ='didiy'

new_phonetic_name = []

# step two: create a loop that will run on the dict
for letter in name.upper():
    for code_letter, code_names in index_phonetic_alphabet.items():
        if letter == code_letter:
            new_phonetic_name.append(code_names)
print('For loop:', new_phonetic_name)
#
# name_letters = [code_names for letter in name.upper() for (code_letter, code_names) in index_phonetic_alphabet.items()
#                 if letter == code_letter]
# print('List Comprehension:', name_letters)

# Try to create the dictionary comprehension without using the 'index_phonetic_alphabet'






