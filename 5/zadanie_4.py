ivan = {"Рост":180,
        "Цвет":"Красный",
        "Фильм":"Зеленый слоник"
        }

vvod = input("Что ты хочешь узнать?")
if vvod in ivan:
    #vyvod = ivan[vvod] 
    print(ivan[vvod])
else:
    print("Такое о себе я ещё не добавил.")
