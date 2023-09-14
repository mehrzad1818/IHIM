#Section 11

#Homework 6
import random
#Way 1
def my_func1(length, number):
    lst = []
    for i in range(length):
        lst.append(random.randint(1, number-1))
    return lst

#Way 2
number = 10
length = 5
lst = range(1, number)
result = random.choices(lst, k = length)
print(result)

def my_func2(lst):
    numbers = []
    for i in set(lst):
        numbers.append((lst.count(i), i))
    return min(numbers)[1]

#Way 2
print(min(set(lst), key = lst.count))

def my_func3(*args):
    res = []
    for i in args:
        res.append((my_func2(i), i))
    return max(res)

#Way 2
lst1 = [6, 2, 7, 6, 3]
lst2 = [2, 2, 2, 4, 2]
lst3 = [1, 3, 1, 1, 1, 1, 3, 1, 1, 3]
args = (lst1, lst2, lst3)
vec = max(args, key = my_func2)
res = (my_func2(vec), vec)
print(res)

res = []
for i in range(20):
    length = int(input("Enter a length:"))
    res.append(my_func1(length, 100))
print(my_func3(*res))

#%%

#Game 2
import random

inp = input("Singleplayer OR Multiplayer?(s/m)")
if inp.lower() == "m":
    #multiplayer
    numbers = []
    names = []
    player_nums = int(input("How many players?"))
    table = player_nums * 100
    cost = 0.3 * table
    prize = table - cost
    for i in range(player_nums):
        names.append(input("What's your name?"))
        counter = 0
        while True:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            counter += 1
            if dice1 == 6 and dice2 == 6:
                numbers.append(counter)
                break
    print(numbers)
    print(names)
    minimum = min(numbers)
    winner = numbers.index(min(numbers))
    print(f"{names[winner]} wins {prize}$ after {minimum} times")
elif inp.lower() == "s":
    #single player
    coin = int(input("How much money?"))
    start = input("Do you want to start?(y/n)")
    #cost per episode is 15$
    cost = 15
    if coin >= cost:
        while start.lower() == "y":
            coin -= cost
            counter = 0
            while True:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                counter += 1
                if dice1 == 6 and dice2 == 6:
                    if 1 <= counter <= 5:
                        coin += 15
                        print("You won 15$")
                    elif 6 <= counter <= 10:
                        coin += 10
                        print("You won 10$")
                    elif 10 <= counter <= 20:
                        coin += 5
                        print("You won 5$")
                    break
            print(f"You have {coin}$")
            start = input("Do you want to continue?(y/n)")
            if coin < cost:
                print("You Don't have enough money")
                break
    
    else:
        print("You Don't have enough money")
