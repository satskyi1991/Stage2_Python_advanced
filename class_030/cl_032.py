def vector(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    print ('(' +str(x), str(y) + ')', (x**2 + y**2)**0.5 )

vector(0,0,1,1)