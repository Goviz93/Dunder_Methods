"""
    Using dunder methods we can sort the items from a directory list by name and type.

    Course: Python objects with special methods - Create better classes!.
    Section: 3 Equality Operators.
    Chapter: 13. Hash.

    * Note: The hash of an object must never change during its lifetime.
        - Numbers will always contain the same hash.
        - Strings will contain a different hash every single session
"""


#Show the hash behavior with numbers.
a = 10
print(hash(a))

b = 0.1
print(hash(b))

c = 347268.3465
print(hash(c))


#Show the hash behavior with strings.
s = "Hello"
print(hash(s))
print("\n\n\n -----------------------------------------------------\n\n\n")



class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        return self.emp_id == other.emp_id

    def __hash__(self):
        return self.emp_id

"""
    e1 is used as a key in the buddies dictionary.
    When a class is used as a key and it define the __eq__ dunder method it must to have __hash__ method too.
    In other wise python will trow an error.   
    
        buddies = {e1:e2}
        TypeError: unhashable type: 'Employee'
     
"""

e1 = Employee(1, "Vera")
e2 = Employee(2, "Chuck")

buddies = {e1:e2}
print(buddies[e1].name)