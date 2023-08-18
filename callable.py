"""
    The dunder method __call__ makes a class acting like a function.

    Course: Python objects with special methods - Create better classes!.
    Section: 4 Object Creation.
    Chapter: 15. Callable.

    Dunder methods:
        __call__ -> Enables a class act like a function.

"""

#Old way to use it
class UserImageFactory:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def create_user_image(self, user_name):
        print("Access database", self.database_connection)
        return f"Image object for {user_name}"


f = UserImageFactory("sqlite")
image = f.create_user_image("Vera")
print(image)

#using __call__
class UserImageFactory2:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def __call__(self, user_name):
        print("Access database", self.database_connection)
        return f"Image object for {user_name}"

d = UserImageFactory2("Oracle")
image2 = d("Vera")
print(image2)