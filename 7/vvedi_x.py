qs = ["Как тебя зовут?",
      "Твой любимый цвет?",
      "Что ты делаешь?"]

n = 0

while True:
    print("Введи X для выхода")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) %3
