"""

    Course: Python objects with special methods - Create better classes!.
    Section: 6 More Operators.
    Chapter: 21. Bool.

    Dunder methods:
        __bool__ -> Boolean value of an object.


"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return self.name

    def __bool__(self):
        return len(self.name) > 0 and self.salary > 0


AllEmployees = [
    Employee("Vera",0),
    Employee("Chuck", 2000),
    Employee("John",0),
    Employee("Dave", 1000)
]

for e in AllEmployees:
    if e:
        print(e)