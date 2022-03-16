muzykanty = {"Xxxtentacion":["SAD", "Save me", "Joselyn Floors"],
             "Big Baby Tape":["Hockage", "Gimme The Loot", "Bandana"]}

vvod = input("Введите имя исполнителя: ")
if vvod in muzykanty:
    print(muzykanty[vvod])
else:
    print("Я такое не слушаю!")
