
"""
    0In this example code, I'm using dunder method __eq__ to compare two
    different objects.

    Course: Python objects with special methods - Create better classes!.
    Section: 3 Equality Operators.
    Chapter: 11. Equality.

    - Rich comparison methods -
        __eq__  -> Equality.
        __ne__  -> Not Equal. This method is implicit.
        __lt__  -> less than operator.
        __le__  -> less or equal operator.
        __gt__  -> greater than operator.
        __ge__  -> greater or equal operator.
"""

class Todo:
    def __init__(self, todo_id, text):
        self.todo_id = todo_id
        self.text = text

    def __eq__(self, other):
        return self.todo_id == other.todo_id


todos = [
    Todo(1, "Call Harry"),
    Todo(2, "Buy milk"),
    Todo(3, "Read book")
]



json = {"todo_id":2, "text": "Buy milk and cookies"}
updated_todo = Todo(json["todo_id"], json["text"])



print(updated_todo in todos) # __eq__

print(updated_todo not in todos) # __ne__
