import math

class Shape:  
    def area(self):
        raise NotImplementedError("Not implemented!")
    
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
    
    
class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area_of_circle = (self.radius ** 2) * math.pi  
        return area_of_circle 