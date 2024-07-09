from random import randint

# 01

# # Create a list from a str
# # Normal why
# name = 'yossi'
# new_name = []
# for i in name:
#   new_name.append(i)
# print(new_name)
#
# # List comprehension
# new_name_02 = [n for n in name]
# print(new_name_02)
#
# # Create range numbers with list comprehension
# num_range = [numbers for numbers in range(1,6)]
# print(num_range)
#

# 02

# # Print a new list that has names with X letters
names = ['James', 'Robert', 'John', 'Michael']
new_names = []

# for n in names:
#   if len(n) < 5:
#     new_names.append(n)
# print(f'Regular: {new_names}')
#
# # Print a new list that has names with X letters - list comprehension
# new_names_comprehension = [n for n in names if len(n) < 5]
# print(f'Comprehension: {new_names_comprehension}')

# 03

# # Print a new list that has names with X letters and all cups
# for n in names:
#   if len(n) < 5:
#     new_names.append(n.upper())
# print(f'Regular: {new_names}')
#
# # Print a new list that has names with X letters and all cups - list comprehension
# cups_names_comprehension = [n.upper() for n in names if len(n) < 5]
# print(f'Comprehension: {cups_names_comprehension}')
#

# 04
# Print remainder of a division % 2 == 0
# 9, 0, 32, 8, 2, 8, 64, 29, 42, 99

# list_of_strings = input("Write a list of numbers: ").split(',')
# print(list_of_strings)
#
# new_list = []
# for n in list_of_strings:
#     if int(n) % 2 == 0:
#         new_list.append(int(n))
# print(new_list)
#
# new_list_comprehension = [int(n) for n in list_of_strings if int(n) % 2 == 0]
# print(new_list_comprehension)

# 05
# Print only the numbers that exist in both files

#Create a list of randome numbers
# for _ in range(25):
#     value = randint(0, 40)
#     print(value)

list1 = []
list2 = []
result = []

with open('file1.txt') as f1, open('file2.txt') as f2:
    file1 = f1
    file2 = f2.read()

    # for f1,f2 in zip(file1, file2):
    #     list1.append(int(f1))
    #     list2.append(int(f2))
    #     if f1 in f2:
    #         result.append(int(f1))

    for n in file1:
        print(n)
        if n in file2:
            print(n)
            result.append(int(n))

    # print(list1)
    # print(list2)
    print(result)


    # Same solution but as a List Comprehension
    # x = [int(f1) for f1, f2 in zip(file1, file2) if f1 in f2]
    # print(x)
