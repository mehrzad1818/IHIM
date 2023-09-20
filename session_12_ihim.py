"""Here we will learn how to open files in Python"""


file = open("Insert the address here.", mode="r")
text = file.read()

print(text)
file.close()


# 1. Use double backslashes in your address
# 2. Change all backslashes to forward slashes.
# 3. put r before the address.


# Reading multiple lines:


file - open("YOur address here")
text = file.readline()
print(text)


# Way 2:

file = open(r";sdjsdjfsdif")
lines = file.readlines()
print(lines)
file.close()


# Way Jadid


file = open(r"sdfnljskgsflgsf")
file.write("hellooooooo")
file.close()


# New way of writing in a file.


file = open(r"adhkfakjfakdjfad")
text = "Hello Guys!\nI'm this person.\nHow are you doing?"
file.write(text)
file.close()

file.writelines()


# HOw to append text to an already existing file


file = open(r"skdlfksdjlskj", mode="a")
text = "hello guys how are you doing."
file


# Pickle Mode

# %%
# import pickle

# dct = {12: 2344, 234: 2345, 234: 234, 9348: 234}
# with open("D:\dictionray.pkl", mode="wb") as file:
#     pickle.dump(dct, file)

# %%
import pandas as pd

pd.read_csv(r"D:\googleplaystore.csv")

# Learn Pandas (Okay?)
# %%

# matplotlib
# pandas
# numpy


# with open(r"D:\python\test.txt") as file:
#     text = file.read()
#     lowered_text = text.lower()
#     this_text = lowered_text.replace("python", "java")

# with open(r"D")


# %%

# OBJECT Oriented Programming




class Person():
    