def divide (x,y, printing):
    def print_result(val):
        if printing:
            if val is None:
                print('Деление на 0 запрещено')
            else:
                print("Резултат деления", val)

    if y == 0:
      result = None
    elif  isinstance(x, int) and isinstance(y, int):
        result =  (x//y)
        print_result(result)
    else:
        result = x/y
        print_result(result)
    return result

printing  = True
print(divide(5,2, printing = True))