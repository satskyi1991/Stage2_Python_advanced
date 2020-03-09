
class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_z(self):
        return self._z

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        return Point(x,y,z)

    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        return Point(x,y,z)

    def __mul__(self, other):
        x = self._x * other._x
        y = self._y * other._y
        z = self._z * other._z
        return Point(x,y,z)

    def __div__(self, other):
        x = self._x / other._x
        y = self._y / other._y
        z = self._z / other._z
        return Point(x,y,z)

    def __neg__(self):
        x = -self._x
        y = -self._y
        z = -self._z
        return Point(x,y,z)

Point1 = Point(1,2,3)
print (Point1.get_x())
print (Point1.get_y())
print (Point1.get_z())

point3 = Point1 + Point1
print(point3._x, point3._y, point3._z)

point3 = Point1 * Point1
print(point3._x, point3._y, point3._z)

point3 = -Point1
print(point3._x, point3._y, point3._z)