class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("Я фигура")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
        print("Прямоугольник создан!")

    def calculate_perimetr(self):
        return 2 * (self.width + self.len)

class Square(Shape):
    def __init__(self, a):
        self.side = a

    def calculate_perimetr(self):
        return self.side * 4
    
    def change_size(self, n):
        self.side = self.side + n

a_rectangle = Rectangle(2, 5)
a_square = Square(2)

a_rectangle.what_am_i()
a_square.what_am_i()
