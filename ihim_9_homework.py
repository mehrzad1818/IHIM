
class Stack:
    """Stack Object in Python"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds the given object to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top object from the stack."""
        try:
            if self.is_empty():
                raise IndexError("Stack is empty.")
            return self.stack.pop()
        except IndexError as error:
            print(str(error))
            return None

    def size(self):
        """Returns the number of objects in the stack."""
        return len(self.stack)

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def __str__(self):
        """Returns a string representation of the stack."""
        return str(self.stack)


stack = Stake()


stack.push(1)
print(stack)
print(stack.is_empty())
# print(stack.__str__())
