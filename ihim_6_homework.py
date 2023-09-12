"""This file contains the 6th homework of IHIM Python course."""
# %%

# Exercise A

import random


def less_than_the_number(numbers, length):
    """Does something"""

    less_than_length = []

    for num in numbers:
        if num < length:
            less_than_length.append(num)

    if less_than_length:
        return random.choice(less_than_length)
    else:
        return None


numbers = input("Enter a list of numbers: ").split()
numbers = [int(num) for num in numbers]

length = int(input(("Enter a length: ")))

random_number = less_than_the_number(numbers, length)
print(random_number)

# %%

# Exercise B


def minimum(*numbers):
    """Find the least occurred number."""
    my_dict = {}

    for number in numbers:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1

    minimum_number = min(my_dict.items(), key=lambda x: x[1])
    return minimum_number


print(minimum(2, 4, 3, 2, 4, 2, 4, 3, 2, 6, 7))

# %%

# Exercise C


def minimum(*numbers):
    """Find the least occurred number."""
    my_dict = {}

    for number in numbers:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1

    # minimum_number = max(my_dict.items(), key=lambda x: x[1])
    minimum_number = max(my_dict.keys()), min(my_dict.values())

    return minimum_number


print(minimum(2, 4, 3, 2, 4, 2, 4, 3, 2, 6, 7))

# %%

# Exercise 2

from random import randint


counter = 0
numbers = []

while counter < 20:
    x = randint(1, 100)
    counter += 1
    numbers.append(x)


def minimum(numbers):
    """Find the least occurred number."""
    my_dict = {}

    for number in numbers:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1

    minimum_number = min(my_dict.items(), key=lambda x: x[1])
    return minimum_number


minimum(numbers)


# %%

# Range function revisited
"""
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
step = int(input("Enter the step value: "))

result = []

if step > 0:
    number = start

    while number < stop:
        result.append(number)
        number += step

elif step < 0:
    number = start

    while number > stop:
        result.append(number)
        number += step

# elif step == 0:
#     print("Step can't be zero.")


print(result)

"""
# %%
"""

# Zip function revisited


list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]

min_length = min(len(list_1), len(list_2))

for i in range(min_length):
    x = list_1[i]
    y = list_2[i]

    print(x, y)

"""
