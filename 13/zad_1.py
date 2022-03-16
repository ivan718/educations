class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
        print("Прямоугольник создан!")

    def calculate_perimetr(self):
        return 2 * (self.width + self.len)

class Square():
    def __init__(self, a):
        self.side = a

    def calculate_perimetr(self):
        return self.side * 4
    
    def change_size(self, n):
        self.side = self.side + n

a_rectangle = Rectangle(2, 4)
print(a_rectangle.calculate_perimetr())

a_square = Square(5)
print(a_square.calculate_perimetr())

a_square.change_size(-1)
print(a_square.side)

