# LISTS ARE MUTABLE
# Lists are sequenced
# subscriptable
# iterable

lst = [3, 3, 3, 3, 324]
print(len(lst))
print(sum(lst))


# lists are compared by their earlist value on the list.
# That is, it goes from top to the bottom and looks for the value which is different.


ls1 = [4, 5, 7]
ls2 = [4, 6, 7, [12, 23]]

x = ls1 > ls2
y = ls2 > ls1

print(x, y)


#%%
#################################################################

# Indecies in python are started from zero

#      0   1    2   3    4   5  6
lst = [1, 1.2, 58, True, 7, 10, 5]
#      -7  -6  -5  -4   -3  -2 -1


#subscriptable types are accessed with square brackets.

number = lst[3]
type(number)

# "Analogy"

Analogy = """agar az har type ye boresh bezanid hamun type ro migirid.
            age ye bakhshi az ye ozv ro begirid hamun type ro migirid"""


number = lst[0: ]


print(lst[2])
10[0] # Error Given
print(lst[8])
print(lst[14]) # Error
print(lst[4:50])
print(lst[:4])
print(lst[2:])
print(lst[2:545445])


#slicing
# list[start:stop]

# %%

lst = [1, 2, 3, 5]
x = (len(lst))
last_digit = lst[x - 1]
print(last_digit)

# lst[-1::-1] or lst[::-1]



# %%

# tamrine avval (ruye kaghaz lazeme)

x = 25
y = 14
z = 12
d = x // y
m = x ** 2
x = m
d *= 1
x = y
print(x, y, d, m)