"""This is session 9 of IHIM python."""
# %%

d1 = {1: "a", 2: "b", 3: "c", 4: "d"}
d2 = {2: "e", 4: "f", 5: "g"}


d1_key = list()
d1_value = list()

for key, value in d1.items():
    d1_key.append(key)
    d1_value.append(value)

d2_key = list()
d2_value = list()

for key, value in d2.items():
    d2_key.append(key)
    d2_value.append(value)

intersection = {}

for key, value in d1.items() and d2.items():
    print(key, value)
# %%


# start = int(input("Enter the start value: "))
# stop = int(input("Enter the stop value: "))
# step = int(input("Enter the step value: "))


def my_range(start, stop=None, step=1, *args):
    """My range function, that i've just built in the class."""

    result = []
    if stop is None:
        stop = start
        start = 0

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

    elif step == 0:
        print("Step can't be zero.")

    return result


print(my_range(100, 50, -2.5))

# Comparison with a list

listy = []
for i in range(100, 50, -2.5):
    listy.append(i)
print(listy)


# %%


from timeit import timeit


CODE1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return age / 10


try:
    calculate_x_factor(0)
except ValueError as this_error:
    print(this_error)
"""

CODE2 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return age / 10


try:
    calculate_x_factor(0)
except ValueError as this_error:
    pass
"""

CODE3 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return age / 10

x_factor = calculate_x_factor(0)
if x_factor == None:
    pass
"""

print("It takes:", timeit(CODE1, number=1000))
print("It takes:", timeit(CODE2, number=1000))
print("It takes:", timeit(CODE3, number=1000))

# %%


def my_zip(*kolli):
    for i in kolli[0]:
        print(i)
        for j in range():
            print(j)


kolli = ((["a", "b", "c"]), ([1, 2, 3]))

my_zip(kolli)

# %%
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]

min_length = min(len(list_1), len(list_2))

for i in range(min_length):
    for j in 
    x = list_1[i]
    y = list_2[i]

    print(x, y)
