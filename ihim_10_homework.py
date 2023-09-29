
class Set:
    """Is basically set without being set."""

    def __init__(self):
        self.items = []

    def add(self, item):
        """Adds an item to the set."""
        if item not in self.items:
            self.items.append(item)
        return self.items

    def delete(self, item):
        """Removes an item from the set if it exists."""
        if item in self.items:
            self.items.remove(item)
        return self.items

    def union(self, other_set):
        """Returns a new set that is the union of the current set and another set."""
        new_set = Set()
        new_set.items = self.items.copy()
        for item in other_set.items:
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        """Returns a new set that is the intersection of the current set and another set."""
        new_set = Set()
        for item in self.items:
            if item in other_set.items:
                new_set.add(item)
        return new_set

    def symmetric_difference(self, other_set):
        """Returns a new set that is the symmetric difference of the current set and another set."""
        new_set = Set()
        for item in self.items:
            if item not in other_set.items:
                new_set.add(item)
        for item in other_set.items:
            if item not in self.items:
                new_set.add(item)
        return new_set

    def copy(self):
        """Returns a new set that is a copy of the current set."""
        new_set = Set()
        new_set.items = self.items.copy()
        return new_set


my_set = Set()


print(my_set.add(25))

# %%


class Graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.coordinates(self.x, self.y)

    def length(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

    def incline(self):
        return self.y / self.x


my_graph = Graph()

my_graph
