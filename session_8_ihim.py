# %%

text = "food"
uniqueL_letter = set(text)
lst = []

for letter in uniqueL_letter:
    lst.append(text.count(letter))
lst.count(max(lst))

maximum = max(lst)
if lst.count(maximum) == 1:
    for i in uniqueL_letter:
        if text.count(1) == maximum:
            text = text.replace(letter, "@")


# %%


def my_func(x, y):
    """This is a calculator. Okay?"""

    return x + y


my_func(10, 5)
my_func(10, 5, 6)
my_func(10)


def my_func(x, y, z=5):
    return x + y + z


my_func(12, 23, 234)

# %%


def multiply(*this):
    """it multiplies"""

    fact = 1
    for number in this:
        fact *= number
    return fact


multiply(2, 3, 4)

# %%

# Mapping


lst = [12, 324, 34, 257]


def my_func(number, power):
    return number**power


out = list(map(my_func, lst, [2, 3, 5, 0]))
print(out)

# %%

import itertools


# %%


# Tamrin 7

# Rewrite range o zip

range


start = input("What's your start? ")
stop = input("What's your stop? ")
step = input("What's your range? ")


start = 0


stop = 50

while True:
    start += start
