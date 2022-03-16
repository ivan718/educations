import math

class Triangle():
    def __init__(self, a, b, c):
            self.sideA = a
            self.sideB = b
            self.sideC = c
            print("Треугольник создан!")

    def height(self):
        poluPerimetr = (self.sideA + self.sideB + self.sideC) / 2
        return((2 * math.sqrt(poluPerimetr * (poluPerimetr - self.sideA) * (poluPerimetr - self.sideB) * (poluPerimetr - self.sideC))) / self.sideA)
        

    def area(self, h):
        self.height = h
        return(0.5 * self.sideA * self.height)

treug = Triangle(8, 4, 6)
print(treug.height())
print(treug.area(treug.height()))



        #poluPerimetr = (self.sideA + self.sideB + self.sideC) / 2
        #((2 * math.sqrt(poluPerimetr * (poluPerimetr - self.sideA) * (poluPerimetr - self.sideB) * (poluPerimetr - self.sideC))) / self.sideA)
