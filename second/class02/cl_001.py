class Vehicle:
    def __init__(self, wheels, motor, color, doors, type):
        self._wheels = wheels
        self._motor = motor
        self._type = type
        self._doors = doors
        self._type = type

        def get_wheels(self):
                return self._wheels

        def set_wheels(self):
            return self._wheels

        def get_color(self):
            return self._color

        def set_color(self):
            return self._color

        def get_motor(self):
             return self._motor

        def set_motor(self):
            return self._motor

        def get_doors(self):
            return self._doors

        def set_doors(self):
            return self._doors

        def get_type(self):
            return self._type

        def set_type(self):
            return self._type


class Car(Vehicle):
    def __init__(self, wheels, motor, color, doors, type, motortype, bodycase):
        self._motortype = motortype
        self._bodycase = bodycase
        super().__init__(wheels, motor, color, doors, type)

    def move(self):
        super.move()
        print(f'{self._wheels} {self._doors}')

class CargoCar(Vehicle):
    def __init__(self, wheels, motor, color, doors, type, motortype, bodycase):
        self._motortype = motortype
        self._bodycase = bodycase
        super().__init__(wheels, motor, color, doors, type)


