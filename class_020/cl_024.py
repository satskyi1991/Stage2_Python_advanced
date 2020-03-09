x = int(input("Введите положительное число: "))
fact =1
i = 1
while i <= x:
    fact *=i
    i+=1
print(x, '!=', fact)