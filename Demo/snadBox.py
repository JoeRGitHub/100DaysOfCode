
import random

# a = []
# def generate_different_numbers():
#     # Generate the first random number
#     num1 = random.randint(0, 50)
    
#     # Keep generating a new random number until it is different from the first one
#     while True:
#         num2 = random.randint(0, 50)
#         if num2 != num1:
#             break
    
#     return num1, num2

# number1, number2 = generate_different_numbers()
# oneNum = number1
# twoNum = number2
# a.append(oneNum)
# a.append(twoNum)

# print(a)
# random.shuffle(a)
# print(a)

def generate_different_numbers():
    dbRandomNumber = {'key': 0} 
    print(f"before{dbRandomNumber['key']}")
    x = 0 #17
    print(x)
    while dbRandomNumber['key'] == x: # 0 == 0
        print('middle')
        x = random.randint(0, 1)
    else:
        dbRandomNumber['key'] = x
        return x

#x = generate_different_numbers()
print(f"after{generate_different_numbers()}")

# for i in range(0,50):
#     x = random.randint(0, 50)
#     if i == x:
#         print('Yes')
#     else:
#         print('No')
# #num1 = random.randint(0, 50)