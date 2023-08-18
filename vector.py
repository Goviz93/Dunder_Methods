"""
    0n this example code, I'm using dunder methods to compare two
    different objects and know if one is greater than or less than.

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


import math

class Vector2:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def magnitude(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()


#v1= Vector2(0,0,2,2) #magnitude 2.828
v1= Vector2(0,0,4,3)
v2 = Vector2(0,0,4,3) #magnitude 5

print(v1.magnitude())
print(v2.magnitude())



#compare the magnitudes
"""
    The following comparison will rise an error:
    print(v1 < v2)
    
        TypeError: '<' not supported between instances of 'Vector2' and 'Vector2'  
        
    To avoid that error we can use __lt__ "less than operator" and use the comparator print(v1 < v2)
    Also, we can use print(v1 > v2) without use __gt__ because it's a reflection of __lt__.
    
    __le__ anable 
"""

print(v1 < v2)
print(v1 > v2)
print(v1 >= v2)
print(v1 <= v2)

