x = int(input("Введите максмальное значение счетчика"))
for i in range(x+1):
    if(x<2):
        continue
    elif(x>5):
        break
    else:
        print(i)
else:
    print("Else")