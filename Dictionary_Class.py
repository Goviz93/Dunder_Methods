"""
    The dunder method __len__ makes a class return its own len.

    Course: Python objects with special methods - Create better classes!.
    Section: 5 Container objects.
    Chapter: 17. Subscriptable

    Dunder methods:
        __getitem__ -> Get an item from an object.
        __setitem__ -> set an item into an object.

"""


class SimpleDictionary:
    def __init__(self):
        self.array = [None] * 10  #Create 10 empty slots.

    def __setitem__(self, key, value):
        # Create an index from a hash generated by the key. And get the module
            # of the hash using the len of the array to get a hash in a range of 0-9.
        index = hash(key[0]) % len(self.array)
        print(index)
        #self.array[index] = value

    def __getitem__(self, item):
        # Create an index from a hash generated by the key. And get the module
            # of the hash using the len of the array to get a hash in a range of 0-9.
        index = hash(item[0]) % len(self.array)
        print(index)
        return self.array[index]

d = SimpleDictionary()
d["Vera"] = 2000 #Map Vera to salary $2000.

print(d["Vera"])