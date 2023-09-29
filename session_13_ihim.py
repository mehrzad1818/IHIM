"""This is the session 13 of IHIM class."""

name = "reza"
try:
    file = open(f"{name}.txt")
except:
    print("File not found.")
    file = open(f"{name}.txt", mode=w)
    file.close()


####
name = "ali"
n = 3


def head(name, n):
    file = open(f"{name}.txt")
    lines = file.readline()
    if len(lines) < n:
        text = "".join(lines)
    else:
        text = "".join(lines[:n])
    return text


def head(name, n):
    file = open(f"{name}.txt")
    lines = file.readline()
    if len(lines) < n:
        text = "".join(lines)
    else:
        text = "".join(lines[:n])
    return text


# ye moshkeli ke tuye code bud in bud ke
# vaqti splice mikonim az ye list, bayad intori bashe ke
# akharesh avaz beshe, yaani chi?
#  masala in list ro bebin: 1 2 3 4 5 6 7 8 9 10

# age man tail 3ta akhar ino bekham, bayad behem 8 o 9 o 10 ro bede
# na inke behem 10 o 9 o 8 ro bede


def showr(name, n):
    file = open(f"{name}.txt")
    lines = file.readlines()
    if len(lines) <= n:
        text = "".join(lines)
    else:
        lst = random.choices(lines, k=n)
    return text


def showall(name):
    file = open(f"{name}.txt")
    return file.read()


try:
    print(head(name, 3))
except:
    print("file is not there.")
# %%


class Stake:
    def __init__(self):
        self.s = []

    def push(self, m):
        self.s.insert(0, m)

    def pop()
