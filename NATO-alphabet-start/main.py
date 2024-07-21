# TODO 1. create a dict in this format:
# {"A": "Alfa", "B", Bravo}

# TODO 2. The user writes text and each letter is translated into a phonetic alphabet:
# Thomas
# ['Tango', 'Hotel', 'Oscar']

# Working with pands
import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
index_phonetic_alphabet = df.set_index('letter')['code'].to_dict()
#print(index_phonetic_alphabet)

name = input("Enter the name you need in your alphabet: ")
#name ='didiy'

new_phonetic_name = []

for letter in name.upper():
    for code_letter, code_names in index_phonetic_alphabet.items():
        if letter == code_letter:
            new_phonetic_name.append(code_names)
print(new_phonetic_name)

name_letters = [code_names for letter in name.upper() for (code_letter, code_names) in index_phonetic_alphabet.items()
                if letter == code_letter]
print(name_letters)


