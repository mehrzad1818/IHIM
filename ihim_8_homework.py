# Homework 8 (No class implementation)

import random


def read_file(file_address):
    """Returns the content of a file."""
    try:
        with open(file_address, mode="r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{file_address}' does not exist. Creating a new file.")
        with open(file_address, mode="w", encoding="utf-8") as file:
            return []


def head(texts, number_of_lines):
    """Returns the given number of lines from the beginning of a text."""
    return texts[:number_of_lines]


def tail(texts, number_of_lines):
    """Returns the given number of lines from the end of a text."""
    return texts[-number_of_lines:]


def show_random(texts, number_of_lines):
    """Returns a random of given number of lines from a text."""
    return random.choices(texts, k=number_of_lines)


def show_all(texts):
    """Returns all lines from a text."""
    return texts


file_address = input("Enter file address: ")
number_of_lines = int(input("How many lines do you need? "))

texts = read_file(file_address)

print(head(texts, number_of_lines))
print(tail(texts, number_of_lines))
print(show_random(texts, number_of_lines))
print(show_all(texts))

# %%

# Homework 8 (with Class Implementation)

import random


class Text_Reader:
    """Contains different modules to perform a variety of tasks on text files."""

    def __init__(self, file_address):
        """Starts the TextReader with the content of a file."""
        self.file_address = file_address
        self.texts = self.read_file()

    def read_file(self):
        """Returns the content of the file."""
        try:
            with open(self.file_address, mode="r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File '{self.file_address}' does not exist. Creating a new file.")
            with open(self.file_address, mode="w", encoding="utf-8") as file:
                return []

    def head(self, number_of_lines):
        """Returns the given number of lines from the beginning of the text."""
        return self.texts[:number_of_lines]

    def tail(self, number_of_lines):
        """Returns the given number of lines from the end of the text."""
        return self.texts[-number_of_lines:]

    def show_random(self, number_of_lines):
        """Returns a random of given number of lines from the text."""
        return random.choices(self.texts, k=number_of_lines)

    def show_all(self):
        """Returns all lines from the text."""
        return self.texts


file_address = input("Enter file address: ")
number_of_lines = int(input("How many lines do you need? "))

text_reader = Text_Reader(file_address)

print(text_reader.head(number_of_lines))
print(text_reader.tail(number_of_lines))
print(text_reader.show_random(number_of_lines))
print(text_reader.show_all())
