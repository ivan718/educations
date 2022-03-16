class Ball:
    def __init__(self, name):
        self.name = name

b1 = Ball("Футбольный")
b2 = b1
print(b1 is b2)

b3 = Ball("Волейбольный")
print(b1 is b3)

b4 = Ball("Футбольный")
b4 = b1
print(b1 is b4)

def proverka(z1, z2):
    return z1 is z2

print(proverka(b1, b3))
