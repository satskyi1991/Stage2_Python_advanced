
x = int(input("Введите положительное число: "))
fact =1
for i in range(1, x+1):
    fact *=i
print(x, '!=', fact)