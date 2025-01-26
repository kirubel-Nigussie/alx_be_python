
import math
class Shape:
    def __init__(self):
        pass
    def area(self):
       raise NotImplementedError("Area method not implemented for this shape.")
    
class Rectangle(Shape):
     def __init__(self, length , width ):
         super().__init__()
         self.length = length
         self.width = width
     def area(self):
       return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()  
        self.radius = radius
    def area(self):
       return math.pi *(self.radius **2)
    





# animals = [Dog(), Animal()]
# for animal in animals:
#   animal.make_sound()  # Output: Woof! (for Dog), Generic animal sound (for Animal)