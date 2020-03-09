x= None
while x is None:
    try:
        x = int(input("Введите делимое число спичек на столе: "))
    except ValueError:
        pass
while x > 0:
    i = 0
    x1 = 0
    for i in range (1,3,1):
        print("Игрок ", i)
        x1 = int(input("Введите число спичек от 1 до 3, которые нужно извлечь: "))
        if x1<1 or x1>3:
            print("Игрок", i, "Ввел неправильное число")
            x1=0
            i -=1
            continue
        else:
            x -= x1
        print ("Осталось", x, 'спичек')
        if x <= 1:
            print("Игрок", i, "Проиграл")
        break
exit()
