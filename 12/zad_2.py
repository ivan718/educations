import math

class Circle():
    def __init__(self, r):
        self.radius = r
        print("Круг создан")

    def area(self):
        return(self.radius ** 2 * math.pi)

krug = Circle(4)
print(krug.area())
