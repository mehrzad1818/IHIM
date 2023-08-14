"""This is session 5 files."""

# Loops (While and For)

"""
while: # condition (Always True or False (Boolean Value))
"""


i = 1
limit = 10

while i <= limit:
    print(i, "Hello.")  # Loop of death (infinite loop)


i = 1
limit = 10

while i <= limit:
    print(i, "Hello.")
    i += 1  # The correct form is this.


for mark in range(5):
    print(mark * "+")

i = 1
limit = int(input("How many instances do you want?\n"))
pattern = int(input("What kind of pattern do you want?\n"))
while i <= limit:
    print(i * pattern)
    i += 1  # The correct form is this.
while i > 1:
    print(i * pattern)
    i -= 1


# Pay attention to types when you bring data from disparate sources.

number = int(input("What is your number baby?\n"))
# %%

# Summation 1 to 100

i = 1
limit = 1000
lst = []

while i <= limit:
    lst.append(i)
    i += 1
print(lst)

# %%

i = 1
limit = 1e10
summation = []


while i <= limit:
    i += 1
    summation.append()
# %%


from time import time

start = time()

i = 1
limit = 1e7
summation = []


while i <= limit:
    i += 1
    summation.append(i)


print(sum(summation))

stop = time()

print(f"Total time is: {round((stop - start), 5)} seconds.")

# %%

from time import time

start = time()

i = 1
limit = 1e7
summation = 0


while i <= limit:
    i += 1
    summation += i


print((summation))

stop = time()

print(f"Total time is: {round((stop - start), 5)} seconds.")

# %%


from time import time

start = time()

number = 1e7
formula = (number * (number + 1)) / 2

print(formula)
stop = time()

print(f"Total time is: {round((stop - start), 5)} seconds.")


# %%
i = 1
number = 5
fact = 1

while i <= number:
    fact *= i
    i += 1
    print(fact)
# %%


from time import time

start = time()

sum((range(1, int((1e8 + 1)))))
print(formula)
stop = time()

print(f"Total time is: {round((stop - start), 5)} seconds.")

# %%


# For loop

# for i in iterable:
#     do this
#     then do this
#     and finally do this


lst = [12, 435, 324, 345]
for in in lst:





number = 5
fact = 1
for i in range(1, number + 1):
    fact *= i
    print(fact)



pattern = "*"
for i in (range(10)):
    line = (2*i - 1) * pattern
    line = line.center(2*limit-1)
    print(line)
tail = "*".center(2*limit-1)


lst = [1, 2, 4, 6, "Hello", 34, 242, 432]
for i in lst:
    if i == "Hello":
        print(i)
        break
    print(i**2)

lst = [1, 2, 4, 6, "Hello", 34, 242, 432]
for i in lst:
    if i == "Hello":
        print(i)
        continue
    print(i**2)