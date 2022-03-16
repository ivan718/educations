import cubed

try:
    a = input("Введите число: ")
    a = int(a)
    print(cubed.chislo_v_kub(a))

except(ValueError):
    print("Введены буквы, а нужно ввести число.")
