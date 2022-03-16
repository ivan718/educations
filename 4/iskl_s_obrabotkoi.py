a = input("Введите число: ")
b = input("Введите ещё одно: ")

a = int(a)
b = int(b)

try:
    print(a / b)
except ZeroDivisionError:
    print("b не может быть нулём.")
