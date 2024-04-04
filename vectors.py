class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
vector1 = Vector(5,6)
vector2 = Vector(2,3)

vector3 = vector1 + vector2

print(vector3)