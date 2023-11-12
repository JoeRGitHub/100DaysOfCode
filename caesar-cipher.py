# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# import math


# def call_func():
#   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#   what_def = input("'encode' or 'decode'? ")
#   word = input("Add a word you wish to convert: ")
#   shift = int(input("Enter a number to shift: "))
#   check = 'no'

#   if shift > len(alphabet):
#     more_then_alphabet = shift / len(alphabet) # 100 / 26 = 74
#     alphabet = alphabet * math.ceil(more_then_alphabet)

#   if what_def == 'encode':
#      encode(word_to_convert=word,num_to_shift=shift, alphabet =alphabet)

#   elif what_def == 'decode':
#      decode(word_to_convert=word,num_to_shift=shift, alphabet=alphabet)

#   check = input("\nRun cipher again? type yes/no: ")

#   if check == 'yes':  #loop back to the start
#       return call_func()
#   print("ByBy")


# def encode(word_to_convert,num_to_shift, alphabet):
#     decrypt_encrypt_word = ""

#     for let in word_to_convert:
#       if let in alphabet:

#         x = alphabet.index(let) # y=24
#         cal = x + num_to_shift  #24 + 2 = 26

#         if cal == len(alphabet): # if 'shift' = 1 or 2
#           cal = 0
#           decrypt_encrypt_word += alphabet[cal]
#         elif cal > len(alphabet): # if 'shift' > 26
#             new_cal = cal - len(alphabet)
#             decrypt_encrypt_word += alphabet[new_cal]

#         else:
#              decrypt_encrypt_word += alphabet[cal]
#       else:
#         decrypt_encrypt_word += let
#     print(f'Word to Encode: {word_to_convert}')
#     print(f'Encode Result: {decrypt_encrypt_word}')

# def decode(word_to_convert, num_to_shift, alphabet):
#     decrypt_encrypt_word = ""
#     for let in word_to_convert:
#       if let in alphabet:

#         x = alphabet.index(let)
#         cal = x - num_to_shift
#         decrypt_encrypt_word += alphabet[cal]
#       else:
#         decrypt_encrypt_word += let
#     print(f'decode: Word to Decode: {word_to_convert}')
#     print(f'decode: Encode Result: {decrypt_encrypt_word}')

# call_func()


import math
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def user_input_variables():
    global shift, what_def, word, check
    what_def = input("'encode' or 'decode'? ")
    word = input("Add a word you wish to convert: ").lower()
    shift = int(input("Enter a number to shift: "))
    check = 'no'


def shift_more_then_alphabet():
    global alphabet
    if shift > len(alphabet):
        more_then_alphabet = shift / len(alphabet)  # 100 / 26 = 74
        alphabet = alphabet * math.ceil(more_then_alphabet)


def run_cipher():
    global alphabet
    user_input_variables()
    shift_more_then_alphabet()

    if what_def == 'encode':
        encode(word, shift, alphabet)
    elif what_def == 'decode':
        decode(word, shift, alphabet)
    run_cipher_again()


def run_cipher_again():
    check = input("\nRun Cipher again? type yes/no: ")

    if check == 'yes':  # loop back to the start
        return run_cipher()
    print("\n*** See you next time. #Cipher ***")


def encode(word, shift, alphabet):
    decrypt_encrypt_word = ""

    for let in word:
        if let in alphabet:

            x = alphabet.index(let)  # y=24
            cal = x + shift  # 24 + 2 = 26

            if cal == len(alphabet):  # if 'shift' = 1 or 2
                cal = 0
                decrypt_encrypt_word += alphabet[cal]
            elif cal > len(alphabet):  # if 'shift' > 26
                new_cal = cal - len(alphabet)
                decrypt_encrypt_word += alphabet[new_cal]

            else:
                decrypt_encrypt_word += alphabet[cal]
        else:
            decrypt_encrypt_word += let
    print(f'You word to encode: {word}')
    print(f'You encode result: {decrypt_encrypt_word}')


def decode(word, shift, alphabet):
    decrypt_encrypt_word = ""
    for let in word:
        if let in alphabet:

            x = alphabet.index(let)
            cal = x - shift
            decrypt_encrypt_word += alphabet[cal]
        else:
            decrypt_encrypt_word += let
    print(f'You word to decode: {word}')
    print(f'You decode result: {decrypt_encrypt_word}')


run_cipher()
