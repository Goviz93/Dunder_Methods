"""

    Course: Python objects with special methods - Create better classes!.
    Section: 5 Container objects.
    Chapter: 18. Iterable

    Dunder methods:
        __iter__ -> Enable an object iteration.
        __next__ -> Enable iteration in all elements from the object.

"""

class SuperRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        self.current = self.min
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return  self.current
        else:
            raise StopIteration


for x in SuperRange(3,9):
    print(x)

