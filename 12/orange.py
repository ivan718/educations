class Orange:
    def __init__(self, w, c):
        """Вес в граммах"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Создано!")

    def rot(self, days, temp):
        self.mold = days * temp


orange = Orange(6, "Апельсин")
print(orange.mold)
orange.rot(10, 33)
print(orange.mold)

"""
or1 =Orange(10, "Темный апельсин")
or1.weight = 100
or1.color = "Светлый апельсин"
or2 = Orange(4, "Светлый апельсин")
or3 = Orange(8, "Темный апельсин")
or4 = Orange(14, "Желтый апельсин")

print(or1)
print(or2)
print(or3)
print(or4)

print(or1.weight)
print(or1.color)
"""
