number = int(input("Enter a number: "))
if 10 == number:
    print("I love you.")
else:
    print("I hate you.")


# %%

# for with more than one variable


x = [1, 2, 3]

y = [4, 5, 6]

for a, b in zip(x, y):
    distance = a**2 + b**2


# %%


# Ex


text = "Hello This is Python Class"
text1 = text.split()

for word in text1:
    word_count = len(word)
    print(word, word_count)


# %%
text = "Hello this is python class"
txt = ""
for i in text:
    txt += i
    if i == " ":
        print(len(txt) - 1)


# %%


text = "This is a very good python class"
listed = []


for word in text.split():
    listed.append((word, len(word)))
print(listed)

# %%


# Loop in Loop
# Nested loops

num = int(input("What is your number: "))

for line, number in enumerate(range(num + 1)):
    print(number, line="\n")

# %%

limit = 5
start = 0

for i in range(1, limit + 1):
    for j in range(i):
        start += 1
        print(start, end=" ")
    print()

# %%
