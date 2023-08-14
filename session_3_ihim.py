# list methods vs. list funcitons

# methods are dependant, while functions are independant.



hey = ["man", "to", "ma"]
hey.append("jimmy")


dir(list)
dir(hey)


jimmy = "HEy babe"
jimmy.

# dunder


#%%
# append item to list 

            # append()
            # extend()
            # insert()

# remove item from list

            # clear()
            # pop()
            # remove()


# some methods don't have any output, therefore we don't assign them
# they will return None as value.

lst = [1]
lst.append(5)
lst.append([1, 2])

# extend
lst.extend([1, 2])

#insert
lst.insert(1, 10)
lst.insert(9, 10)
lst.insert(len(lst), 10)



######

lst = [1, 1.2, 58, True]

# clear makes a list empty
# lst.clear()

lst.pop()

# by defauly (without defining the inddex), pop removes the last 


lst.remove(True)
lst.remove(1)
lst.remove(True)



# count, literally counts the value in the list.
lst.count(1)
lst.index(True)
lst.index(True, 1)

raise

# count
# intdex
# copy
# reverse
# sort


# copy (shallow copy)

a = [1, 2, 4]
b = a.copy()
c = a[1:]
a[0] = 10
print(a, b, c)


# har type ke method copy() ro dashte bashad, mitavanad mutable bashad.



# reverse()

lst.reverse()


# lst = lst[::-1] == lst.reverse()

# both sort() and reverse() are inplace



lst.sort()
lst.reverse()

lst.sort().reverse()
None.reverse()
lst.sort()[::-1]


# list functions )



# Tuple


# tuple are just like lists, they are sequencable, subscriptable, but they are immutable




tup = (1, 1.2, True, 56)
type(tup)
sum(tup) # Iterable, can bu summed
tup[0] = 10
dir(tuple)

# one item tuple


tup_one = (1)
type(tup_one)

# changing types 


tup = (1, 1.2, True, 58)
tup = list(tup)
tup[tup.index(1.2)] = 10
tup = tuple(tup)
print(tup)




# String - sequencable, subscriptable, iterable


text = "Hello World."
type(text)
len(text)
text[::-1]

text = 10 * "Hello "
text[:-1]

x = "Hi, I'm Ali. "What is your name"."


text1 = ""
text2 = ""
text3 = ""

re # regular expressions

text = "Hello world!"

list(text)
tuple(text)

text = "dfsdf"
text.



