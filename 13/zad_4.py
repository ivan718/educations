class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

mitchell = Rider("Митчелл Скачущий")
pony = Horse("Пони", "Быстрая", mitchell)

print(pony.owner.name)
