s=''
while not s.isdigit():
    s = input('Введите положительное число:')
x = int(s)
print('Дальше будем работать с x ='+s)

print('Вычисление соседних чисел фибоначи для',x)
fib1= 1
fib2= 1
while fib2 < x:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
print(fib1, '<', x, '<=', fib2)