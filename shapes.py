import math

class Shape():
    def __init__(self, w):
        self.w = w
        self.perimeter = 0
        self.surface = 0
    
    def __lt__(self, other):
        return self.surface < other.surface


class Circle(Shape):
    def __init__(self, w):
        super().__init__(w)
        self.perimeter = self.calc_perimeter()
        self.surface = self.calc_surface()
    
    def calc_perimeter(self):
        return math.pi * self.w

    def calc_surface(self):
        return math.pi * (self.w/2)**2

class Square(Shape):
    def __init__(self, w):
        super().__init__(w)
        self.perimeter = self.calc_perimeter()
        self.surface = self.calc_surface()
    
    def calc_perimeter(self):
        return 4*self.w
    
    def calc_surface(self):
        return self.w**2
    

square = Square(10)
circ = Circle(10)

print(square < circ)