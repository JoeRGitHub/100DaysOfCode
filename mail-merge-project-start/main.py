# TODO: Create a letter using starting_letter.txt
# TODO: for each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_path = "./Input/Names/invited_names.txt"
starting_letter_path = "./Input/Letters/starting_letter.txt"
search_word = '[name]'

def search_and_replace(names_path, starting_letter_path, search_word):
    file_name = open(names_path, "r")
    letter = open(starting_letter_path, "r")
    file_contents = letter.read()

    for x in file_name:
        x = x.strip()
        x = x.replace(',','')
        print(file_contents)
        updated_contents = file_contents.replace(search_word, x)
        print(updated_contents)
        with open(f'./Output/ReadyToSend/{x}.txt', 'w') as file:
            file.write(updated_contents)

search_and_replace(names_path, starting_letter_path, search_word)
