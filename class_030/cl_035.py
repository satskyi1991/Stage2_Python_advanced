x= None
while x is None:
    try:
        x = float(input("Введите делимое: "))
    except Exception:
        pass
y = None
while y is None:
    try:
        y = float(input("Ввкдите делитель:"))
    except Exception:
        pass
try:
    print('Результат деления',x, 'на', y, 'равен', x/y)
except ZeroDivisionError:
    print('Деление на ноль!!')