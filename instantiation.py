"""
    The dunder method new isn't used, but __init__ method is used always. Here is an example
    of how to initialize a base class.

    Course: Python objects with special methods - Create better classes!.
    Section: 4 Object Creation.
    Chapter: 14. Instantiation.

    Dunder methods:
        __new__ -> Creates an object memory location and returns a reference to it.
        __init__ -> Does nothing.

"""


# Example for __new__
class Employee:

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        return super().__new__(cls, *args, **kwargs)

e = Employee()

print(e)

print("\n\n\n")



#Example for __init__
class EmployeeBase:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Programmer(EmployeeBase):
    def __init__(self, name, salary, programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language


p = Programmer("Vera", 2000, "Python")
print(f"{p.name} (${p.salary}) programs in {p.programming_language}")

