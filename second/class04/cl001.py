
class Decorators:

    @staticmethod
    def dec(func):
        def wrapper(*args):
            func()
        return wrapper

class A:
    def dec(func):
        def wrapper(*args):
            print(args)
            print(func)
            func(*args)
        return wrapper

    @dec
    def do_smth(self, arg1, arg2):
        pass

a = A()
a.do_smth(1,2)