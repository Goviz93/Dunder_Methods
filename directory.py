"""
    Using dunder methods we can sort the items from a directory list by name and type.

    Course: Python objects with special methods - Create better classes!.
    Section: 3 Equality Operators.
    Chapter: 12. Comparing and sorting.

    - Rich comparison methods -
        __eq__  -> Equality.
        __ne__  -> Not Equal. This method is implicit.

        __lt__  -> less than operator.
        __le__  -> less or equal operator.
        __gt__  -> greater than operator.
        __ge__  -> greater or equal operator.
"""


class DirectoryItem:

    def __init__(self, name):
        self.name = name
        self.is_directory = name.endswith("/")


    def __str__(self): #Enable get the name of the object.
        return self.name

    def __lt__(self, other): #Enable sort items by name.
        if self.is_directory == other.is_directory: #Checks if the name is a name from a directory.
            return self.name < other.name
        return self.is_directory


directory = [
    DirectoryItem("log.txt"),
    DirectoryItem("settings/"),
    DirectoryItem("test.txt"),
    DirectoryItem("archive/"),
    DirectoryItem("config.txt"),
]


for d in sorted(directory):
    print(d)