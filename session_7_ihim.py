"""Session 7"""


# We need to learn the concepts, irrevirsible of the language that it is written in

# When we divide them by 10, the remainder is the each individual number


number = 12345
digits = []

while number != 0:
    remain = number % 10
    digits.append(remain)
    number //= 10
print(sum(digits))




number = 12345
summation = 0

while number != 0:
    remain = number % 10
    digits.append(remain)
    number //= 10
print(sum(digits))



#%%



number = 12345
digits = []

while number != 0:
    remain = number % 10
    digits.append(remain)
    number //= 10



length = len(digits)
for i in digits:
    length -= 1
    if i == 0:
        continue
    res = i * (10**length)
    summation += res

print(summation)


#%%


number = 6
summation = 0


for i in range(1, number):
    if number % i == 0:
        summation += 1

if summation == number:
    print("It's a perfect number.")


# %%




f = lambda x: x**2

# callable

f(10)

10() # Error



%whos



is_even = lambda number: number % 2 == 0
is_even(10)

is_even(5)


even_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


word_counter = lambda text: len(text.split())
word_counter("Hello this is Python class.")


# %%




# matplot
# panda
# numpy
# %%
""


# def


"""
def function_name(inputs):
    function_body

"""
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

even_odd(10)  
even_odd(5)


#%%

# Factorial with functions
def factorial(number):


    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return(fact)

factorial(12)


#%%

# Print vs. Return


 def factorial_printed(number):


    fact = 1
    for i in range(2, number + 1):
        fact *= i
    print(fact)


def factorial_returned(number):


    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return(fact)

print(factorial_printed(5))
print(factorial_returned(5))
# %%
