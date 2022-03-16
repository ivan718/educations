class Apple():
    def __init__ (self, w, c, s, v):
        self.weight = w
        self.color = c
        self.sort = s
        self.vkus = v
        print("Яблоко добавлено!")


aport = Apple(10, "Синий", "Апорт", "Сладкий")

print(aport.vkus)
