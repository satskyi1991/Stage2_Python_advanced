from abc import abstractmethod, ABC


class AbstractVehicle(ABC):

    @abstractmethod
    def drive(self):
        print('Driving')

    @abstractmethod
    def beep(self):
        print('BEEP!')


class Vehicle(AbstractVehicle):
    def __init__(self, model, engine):
        self._model = model
        self._engine = engine

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
from abc import abstractmethod, ABC


# class AbstractVehicle(ABC):
#
#     @abstractmethod
#     def drive(self):
#         print('Driving')
#
#     @abstractmethod
#     def beep(self):
#         print('BEEP!')


class Vehicle(AbstractVehicle):
    def __init__(self, model, engine):
        self._model = model
        self._engine = engine

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def drive(self):
        super().drive()

    def beep(self):
        super().beep()


auto = Vehicle('bmw', 'v6')

auto.model = 'Lanos'
print(auto.model)

# class AbstractVehicle:
#
#     def drive(self):
#         raise NotImplementedError()
#
#     def beep(self):
#         raise NotImplementedError()
#
#
# class Vehicle(AbstractVehicle):
#     pass
#
# a = Vehicle()


# def drive(self):
#     super().drive()
#
# def beep(self):
#     super().beep()


auto = Vehicle('bmw', 'v6')

print(auto.model)


# class AbstractVehicle:
#
#     def drive(self):
#         raise NotImplementedError()
#
#     def beep(self):
#         raise NotImplementedError()
#
#
# class Vehicle(AbstractVehicle):
#     pass
#
# a = Vehicle()
