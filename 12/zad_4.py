class Hexagon():
    def __init__(self, a, b, c, d, e, f):
        self.sideA = a
        self.sideB = b
        self.sideC = c
        self.sideD = d
        self.sideE = e
        self.sideF = f
        print("Шестиугольник создан!")

    def calculate_perimetr(self):
        return(self.sideA + self.sideB + self.sideC + self.sideD + self.sideE + self.sideF)

shestiugol = Hexagon(1, 2, 3, 4, 5, 6)
print("Перимерт шестиугольника = ", shestiugol.calculate_perimetr())
