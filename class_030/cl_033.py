a= 5
del a

def f (x,y):
    global a
    print(x,y,a)
    a = x * y

x = 10
y = 20
a = 5
f(5,6)

print (x,y,a)