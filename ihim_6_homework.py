"""Game and 6"""

# Game
#%%
from random import randint

logo = """
   ___                       _____                  __                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|

"""

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks the player's guess against the answer and returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    """Prompts the player to choose a difficulty and returns the number of turns based on the chosen difficulty."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Runs the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()


#%%




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


print(minimum(2, 4, 3, 2, 4, 2, 4, 3, 2, 6, 6, 7, 7))

#%%
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

