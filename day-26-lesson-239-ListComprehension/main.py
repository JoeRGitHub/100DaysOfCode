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

# TODO: create a script to compare between two files and find the similar numbers
#  and print them in a  list

with open("file1.txt") as file1, open("file2.txt") as file2:
    # x = file1.read().split()
    # y = file2.read().split()
    #
    # result = []
    # for num in x:
    #     if num in y:
    #         result.append(int(num))
    # print(result)

    list1 = file1.readlines()
    list2 = file2.readlines()

result1 = [int(num) for num in list1 if num in list2]
print(result1)

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

weather_c = eval("{'NY': 35, 'JS': 42, 'WDS': 25, 'SD': 23}")

# for name, score in weather_c.items():
#     temp_f = score * 9/5 + 32
#     weather_c[name] = temp_f
# print(weather_c)

convert_c_to_f = {name:score * 9/5 + 32 for (name, score) in weather_c.items()}
print("Convert celsius to fahrenheit:", convert_c_to_f)

##########################################

names = ['James', 'Michael', 'Joe', "David"]

new_score = {new_key:random.randint(1,100) for new_key in names}
print('Names and numbers:', new_score)