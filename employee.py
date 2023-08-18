

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.name} {self.id}"

    def __str__(self):
        return self.name



employees = [
    Employee(1, "Vera"),
    Employee(2, "Chuck"),
    Employee(3, "Dave")
]


for e in employees:
    print(e)