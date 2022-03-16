class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)

    def __repr__(self):
        return "{} на {} на {} на {}".format(self.side, self.side, self.side, self.side)

s1 = Square(2)
s2 = Square(3)
s3 = Square(4)

print(Square.square_list)
print(s1)
