# %%
# Number 1

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")


# %%
# Number 2

numbers = input("Enter a list of numbers (separated by spaces): ").split()

count = 0
for number in numbers:
    if int(number) % 3 == 0:
        count += 1

print("Count of numbers divisible by 3:", count)

# %%
# Number 3

string = input("Enter a string of letters: ")
letter = input("Enter the letter to count: ")

count = 0
for char in string:
    if char == letter:
        count += 1

print("Count of letter", letter, "in the string:", count)


# %%


from timeit import timeit


process1 = """
number = 10000

if number <= 1:
    print(number, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

        
        """
process2 = """
number = 10000

if number <= 1:
    print(number, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

        """


print(timeit(process1, 1000))
print(timeit(process2, 1000))

# %%
