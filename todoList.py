"""
    The dunder method __len__ makes a class return its own len.

    Course: Python objects with special methods - Create better classes!.
    Section: 5 Container objects.
    Chapter: 16. len.

    Dunder methods:
        __len__ -> number of items.

"""


"""
    The dunder method __getitem__ 

    Course: Python objects with special methods - Create better classes!.
    Section: 5 Container objects.
    Chapter: 17. Subscriptable.

    Dunder methods:
        __getitem__  -> object behave like a list. Getting elements from the bject.

"""

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, value):
        self.items.append(value)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        print(item)
        return self.items[item]

todo = TodoList()
todo.add_item("Call Harry")
todo.add_item("Clean sink")
todo.add_item("Read book")

#len
print(f"The list has {len(todo)} items")

#Subscriptable
print(todo[1:3])


