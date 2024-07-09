##########################################

numbers = [1, 2, 3]
new_list = []
new_num = [n + 1 for n in numbers]
print(f'add one to evey number in the list: {new_num}')

##########################################

x = range(1, 5)
new_itme = [n * 2 for n in x]
print(f'multiply range of numbers in 2: {new_itme}')

name_list = ["James", "Michael", "Robert", "John", "David"]
new_name_list = []

##########################################

# for i in name_list:
#     if len(i) > 4:
#         new_name_list.append(i)
# print(new_name_list)

##########################################

check_len = [name for name in name_list if len(name) > 4]
print(f'print only names > 4 letters: {check_len}')

##########################################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers = []

for num in numbers:
    x = num * num
    new_numbers.append(x)
print(f'squared numbers: {new_numbers}')

##########################################

numbers_list_comp = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers_list_comp = [num * num for num in numbers_list_comp]
print(f'list comprehension squared numbers: {new_numbers_list_comp}')

##########################################

# list_of_strings = input("Enter the numbers separated by ',':").split(',')
# # #
# # for i in list_of_strings:
# #     i.replace(" ", "")
# #     x = int(i)
# #     if x % 2 == 0:
# #         new_list.append(int(x))
# # print(f'Print only whole numbers without space: {new_list}')
#
# new_list_of_strings = [int(i.replace(" ", "")) for i in list_of_strings if int(i) % 2 == 0]
# print(new_list_of_strings)

##########################################

# Open both files for reading
with open('file1.txt', 'r') as a, open('file2.txt', 'r') as b:
    content_a = a.read().split()
    content_b = b.read().split()

# Find common elements by checking if each element in content_a is also in content_b
# Convert the common elements to integers and store them in the result list
result = [int(num) for num in content_a if num in content_b]
print(result)

    ## I'm leaving for the record how much trouble I got into just to solve this problem.
    ## In the end the answer was right under my nose.I turned out to be a stupid

    # convert str to int and use split to break the content of the file into individual elements
    # x = [int(i) for i in content_a]
    # y = [int(i) for i in content_b]
    # print("List x:",x)
    # print("List x:",y)

    # At first, I tried to work with zip, but I came to see that it's not good.
    # The comparison is not a list against a list, but a number against a number within the tuple.

    # for i,j in zip(x,y):
    #     if i == j:
    #         print(i)

    # x = [i for i,j in zip(x,y) if i == j]
    # print(x)

    # common_elements = set(x) & set(y)
    # if common_elements:
    #     print(f"Matching numbers: {common_elements}")
    # else:
    #     print("No matching numbers")

##########################################
# Lesson 241:

import random

names = ['James', 'Michael', 'Robert', 'John']
results = {student:random.randint(1,50) for student in names}
print('Dict list of names with their results:',results)

# Create a dictionary of students who scored more than > X
pass_student = {student:score for (student, score) in results.items() if score > 20}
print('Dict list of names with their results more then x: ',pass_student)

##########################################
# Lesson 242:

# sentence = input('Enter a sentence: ')
# #list_of_words = sentence.split()
# #print(list_of_words)
# dict_of_words_cunt = {word:len(word) for word in sentence.split()}
# print(dict_of_words_cunt)

##########################################
# Lesson 243:

weather_c = eval("{'James': 3, 'Michael': 42, 'Robert': 25, 'John': 4}")

# for name, score in weather_c.items():
#     temp_f = score * 9/5 + 32
#     weather_c[name] = temp_f
# print(weather_c)

convert_c_to_f = {name:score * 9/5 + 32 for (name, score) in weather_c.items()}
print(convert_c_to_f)

