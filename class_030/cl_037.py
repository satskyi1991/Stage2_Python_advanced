
def input_int(msg):
    result = None
    while result is None:
        try:
            result = int(input('Введите ' + msg + ' число диапазона :'))
        except ValueError:
            pass
        return result

x1 = input_int('первое')
x2 = input_int('второе')
max = 0
if (x2> x1):
    increment = 1
    max = x2
elif (x1>x2):
    increment = -1
    max = x1
else:
    increment = 0
    max = x1
sum = 0
if max > 0:
    for i in range(min, max, increment):
        sum +=i
        print ("Sum in range", x1, x2, 'with step', increment, '=' , sum  )

print ("Sum in range", x1, x2, 'with step', increment, '=' , sum  )