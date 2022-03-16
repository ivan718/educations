class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

a_rectangle = Rectangle(4, 5)
print(a_rectangle.area())

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)


class PublicPrivateExample:
    def __init__(self):
        self.public = "Безопасно"
        self._unsafe = "Опасно"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass
    
class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Мик Джаггер")
stan = Dog("Стэнли", "Бульдог", mick)

print(stan.owner.name)
