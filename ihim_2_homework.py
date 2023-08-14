"""This program takes an input (number) from
the user and checks whether it is divisible by 5 and 3. """
# %%
# 1
input_number = int(input(f"Input a number:\n{'':>4}"))

if (input_number % 3 == 0) and (input_number % 5 == 0):
    print(f"{input_number} is divisible by both 5 and 3.")
elif input_number % 5 == 0:
    print(f"{input_number} is divisible by 5.")
elif input_number % 3 == 0:
    print(f"{input_number} is divisible by 3.")
else:
    print(input_number)


# %%


# 2
def is_triangle(a, b, c):
    """This function checks whether 3 given sides can make a triangle or not."""
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


a = float(input(f"Enter the first side length:\n{'':>4}"))
b = float(input(f"Enter the second side length:\n{'':>4}"))
c = float(input(f"Enter the third side length:\n{'':>4}"))

if is_triangle(a, b, c):
    print(f"The given sides can form a triangle with the perimeter of {a + b + c}")
else:
    print("The given sides cannot form a triangle.")

is_triangle(a, b, c)


# %%


# def tax_calculator(income):
#     """Finds tax amount according to income. (Predefined numbers.)"""


def percent_finder(income):
    """Calculates the tax."""
    if income < 8925:
        return 10

    if income < 36250:
        return 15

    if income < 87850:
        return 23

    if income < 183250:
        return 28

    if income < 398350:
        return 33

    if income < 400000:
        return 35

    if income >= 400000:
        return 39.6


def tax_profiler(income):
    """Brain of the tax calculator."""

    tax_amount = (income * percent) / 100
    net = income - tax_amount

    return net, tax_amount


income = float(input("Enter your income: "))
percent = percent_finder(income)
net, tax_amount = tax_profiler(income)

print(
    "Here's the output:\n",
    f"{'Gross income:':<20} {income} {'$'}",
    f"{'Tax Rate:':<20} {percent} {'%'}",
    f"{'Tax Amount:':<20} {tax_amount} {'$'}",
    f"{'Net Income:':<20} {net} {'$'}",
    sep="\n",
)

# %%
