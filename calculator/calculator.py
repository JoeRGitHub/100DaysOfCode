
from replit import clear

# import os
# clear = lambda: os.system('clear')
# clear()

def add(a,b):
  return a+b

def minus(a,b):
  return a-b

def multi(a,b):
  return a*b

def divide(a,b):
  return a/b

def get_num():
  return float(input('Add a number: '))
  
def operator():
  return input('\n+\n-\n*\n/\n Select an operator: ')
  
dic_num1 = {}

def calculator(a=None):
  
  get_operator= ''

  if a == None:
    print('Welcome to my calculator!\n')
    num1 = get_num()
    get_operator= operator() 
    num2 = get_num()
  else:
    num1=dic_num1['key']
    get_operator= operator() 
    num2 = get_num() 
  
  if get_operator == '+':
    result = add(num1, num2)
    #print(add(num1, num2))
  elif get_operator == '-':
    result = minus(num1, num2)
    #print(minus(num1, num2))
  elif get_operator == '*':
    result = multi(num1, num2)
    #print(multi(num1, num2))
  elif get_operator == '/':
    result = divide(num1, num2)
    #print(divide(num1, num2))
    
  print(f'{num1} {get_operator} {num2} = {result}')
  dic_num1['key']= result

  i =  input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if i == 'y':
    calculator(a=result)
    print(f'after: {result}')
  else:
    clear()
    calculator(a=None)

result = calculator(a=None)
print(result)

