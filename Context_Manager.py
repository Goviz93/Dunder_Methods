"""

    Course: Python objects with special methods - Create better classes!.
    Section: 6 More Operators.
    Chapter: 20. Context Manager.

    Dunder methods:
        __enter__ -> Magic method when starting a 'with' block
        __exit__ -> Magic method called at the end.

"""

class Logger:
    def __enter__(self):
        print("Open database connection for loggin")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type:", exc_type)
        print("exc_val",exc_val)
        print("exc_tb", exc_tb)
        print("Close database connection")

    def log(self, message):
        print("Log to database: ", message)


with Logger() as log:
    log.log("Start division")
    A = 10
    B = 0
    print(A/B)
    log.log("End division")


print("The end")
