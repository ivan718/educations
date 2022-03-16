chisla = [67, 325, 231, 21, 360]


while True:
    try:
        
        print("Для выхода нажми X")
        guess = input("Введите любое число из списка: ")
        if guess == "X":
            break
        guess = int(guess)
        if guess in chisla:
            print("Верно, вы угадали число.")
        else:
            print("Неверно! Попробуйте ещё раз.")
            
    except(ValueError):
        print("Ошибка ввода!!!")
