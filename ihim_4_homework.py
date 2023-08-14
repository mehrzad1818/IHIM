"""This file contains the fourth homework of Python class. 8/9/2023"""

# %%
### 1.1 This one takes only whole numbers. ValueError is raised if we put decimals.

number = int(input("Enter a whole number: "))
number_stringed = str(number)
summm = 0

for digit in number_stringed:
    summm += int(digit)

print(summm)

# %%
### 1.2 This one takes decimals as well.

number = float(input("Enter a number: "))
number_stringed = str(number)
summm = 0
desired_digits = "0123456789"

for digit in number_stringed:
    if digit in desired_digits:
        summm += int(digit)

print(summm)

# %%
### 1.3 This one takes any input (presumably)

number = float(input("Enter a number: "))
number_stringed = str(number)
summm = 0

for digit in number_stringed:
    if digit.isdigit():
        summm += int(digit)

print(summm)

# %%
### 2

number = input("Enter a number: ")
reversed_number = reversed(number)

for number in reversed_number:
    print(number, end="")


# %%
### 2.2 The same program using list comprehension


number = input("Enter a number: ")

reversed_number = int("".join([digit for digit in str(number)][::-1]))

print(reversed_number)

# %%
### 3.1 Perfect Number

number = int(input("Enter a number: "))


mults = []
for mult in range(1, number):
    if number % mult == 0:
        mults.append(mult)


if sum(mults) == number:
    print("Perfect.")
else:
    print("Try again.")

# %%
### 3.2 Perfect Number (List Comprehension)


number = int(input("Enter a number: "))


mults = [mult for mult in range(1, number) if number % mult == 0]
summed_mults = sum(mults)

if summed_mults == number:
    print("Perfect.")
else:
    print("Try again.")
# %%
