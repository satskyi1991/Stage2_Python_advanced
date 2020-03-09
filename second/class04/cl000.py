


class Point:
    _instances = None
    def __new__(cls, *args, **kwargs):
        if cls._instances:
            return cls._instances
            #raise Exception('It is a singletone type')
        else:
            cls._instances = super().__new__(cls)
            return cls._instances

a = Point()
a.x = 100
print (a.x, Point().x)

class Person:
    fields = ('id_', 'name', 'nickname')
    _instances = None
    def __new__(cls, *args, **kwargs):
        if cls._instances:
            return cls._instances
            #raise Exception('It is a singletone type')
        else:
            cls._instances = super().__new__(cls)
            for field in cls.fields:
                setattr(cls._instances, field,100)

            return cls._instances

#a = Person()
#print(a.id_,a.name,a.nickname)

#b = Point()
#print(a.x, b.x)

# def method():
#     print('Hi')
#
# MyCl = type (
#     'MyClass',
#     (),
#     {
#         'the_first_attr':1,
#         'get_smth' : method
#
#     }
# )
#
# obj_of_my_class = MyCl()
# print(obj_of_my_class.get_smth())
class UsefulMethods:
    def make_class_feel_good(self):
        print('Feel good')

class MyMeta(type):
    def __new__(mcls,name,bases,attributes):

        if '_'in name:
            raise NameError('You Cant name class like this')
        bases += (UsefulMethods, object)
        print(mcls,name, bases, attributes)
        return super().__new__(mcls, name, bases, attributes)

class Point(metaclass = MyMeta):
    print('12134')
    name = 'PointClass'

    def _init(self,x):
        self.x = x

print(Point.__bases__)