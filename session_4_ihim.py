# This is session 4 of IHIM.
# This course will be a total of 13 sessions.


# %%
# format

accuracy = 0.26
number = 23

print("The accuracy is:", accuracy * 100, "Number is:", number - 2)
print("The accuracy is: {}\nNumber is: {}".format(accuracy * 100, 234))
print(f"The accuracy is {accuracy * 100}\n Number is: {number - 2}")

# %%
# replace

text = "Hello World!"
text.replace("l", "*")
text.replace("ll", "*")
text.replace(" ", "-")
text.replace("l", "")
text.replace("l", "*", 2)
text.replace("World", "guys!")

text[::-1].replace("l", "*", 1)[::-1]
number_1 = text.count("l")
text.replace("l", "*").replace("*", "l", number_1 - 1)

text = "Hello WOrld!"
text.center(50)
text.center(10)
text.center(50, "8")
text.center(len(text) + 50)

# %%
# is alpha
text = "Hello World!"
text.isalpha()

# %%
# Dictionary


dicty = {
    "key1": "value",
}

type(dicty)
len(dicty)
dir(dicty)


dicty.pop("key1")

dicty.popitem()


dicty.update({"key1": 10, 4: "four"})
dicty.update(("key1", 34), (4, 45))

# %%
# set


text = "Hello this is python class and the students are doing this"
words = text.split()
unique_words = set(words)

print(f"Number of words is: {len(words)}\nNumber of unique words: {unique_words}")

text = text.lower()
letters = text.replace(" ", "")
unique_letters = set(letters)

print(f"Number of letters is: {len(letters)}\n Number ")


# %%
# Conditional Expressions

# if condition:
#     command1
# elif:
#     command2
# elif:
#     command3
# else:


RAINING = False
if RAINING == True:
    ["This is me"].append(23)
else:

########


number = input("WHat is your number?")

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")



#####


number = 17
if number % 3 == 0:


# Optimization principals:

# 1. Reduce processing cycles.
# 2. Reduce RAM consumption
# 3. Reduce Runtime


# %%
# Class Exercise



number = int(input("What is your number? "))

if number % 5 == 0:
    print("3k")
else:
    if number % 5 == 1:
        print("3k+1")
    else:
        if number % 5 == 2:
            print("3k+2")
        else:
            if number % 5 == 3:
                print("3k+3")
            else:
                print("3k+4")


# %%


if number % 5 == 0:
    print("5k")
elif number % 5 == 0:
    print("5k")
elif number % 5 == 0:
    print("5k")
elif number % 5 == 0:
    print("5k")
else number % 5 == 0:
    print("5k")
