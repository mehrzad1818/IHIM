#Section 10

#zip
lst1 = [1, 2, 3]
lst2 = [4, 5]
text = "Hello"
iterables = (lst1, lst2, text)
number_inp = len(iterables)
size_inp = len(min(iterables, key = len))
result = []
for i in range(size_inp):
    tmp = ()
    for j in range(number_inp):
        tmp = tmp + (iterables[j][i],)
    result.append(tmp)
print(result)

def my_zip(*iterables):
    number_inp = len(iterables)
    size_inp = len(min(iterables, key = len))
    result = []
    for i in range(size_inp):
        tmp = ()
        for j in range(number_inp):
            tmp = tmp + (iterables[j][i],)
        result.append(tmp)
    return result
lst1 = [1, 2, 3]
lst2 = [4, 5]
text = "Hello"
print(my_zip(lst1, lst2, text))
#%%

#list comperhension
lst = [1, 2, 3, 4, 5, 6]
out = []
for i in lst:
    if i % 2 == 0:
        out.append(i**2)
print(out)


lst = [1, 2, 3, 4, 5, 6]
out = [i**2 for i in lst if i % 2 == 0]
print(out)
out = [i**2 if i % 2 == 0 else i for i in lst]
print(out)
#%%

#generator
#yield for functions return generators
lst = [1, 2, 3, 4, 5, 6]
out = (i**2 if i % 2 == 0 else i for i in lst)
type(out)
print(list(out))

def my_func(*args):
    yield args
result = my_func("Hello", 10, 5)
print(list(result))

#%%

#recursive function
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
result = factorial(5)

#%%

#fibonatchi

fib = [0, 1]
limit = 10
for i in range(limit-2):
    fib.append(fib[-1] + fib[-2])
print(len(fib))
print(fib)

#fibonatchi with functions

def fibonatchi(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonatchi(number-1) + fibonatchi(number-2)
fibonatchi(10)

#%%

#library
import math
math.factorial(5)
#%whos
import math as mt
math.factorial(5) #Error
mt.factorial(5)

from math import factorial
factorial(5)

#not recommended
from math import *
from numpy import *
sin()
#%%

#Game 1
import random
secret = random.randint(1, 100)
while True:
    guess = int(input("Enter a number:"))
    if secret > guess:
        print("Greater")
    elif secret < guess:
        print("Lesser")
    else:
        print("BINGO")
        break
#%%

#Game 1 with functions

import random

def compare(guess, secret):
    if guess < secret:
        return 1
    elif secret < guess:
        return -1
    else:
        return 0
def show_messages(compare_result):
    messages = {1: "Greater", -1: "Lesser", 0: "BINGO"}
    print(messages[compare_result])

def game():
    secret = random.randint(1, 100)
    while True:
        guess = int(input("Enter a number:"))
        res = compare(guess, secret)
        show_messages(res)
        if res == 0:
            break
game()
