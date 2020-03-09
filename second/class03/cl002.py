import time
from functools import wraps

# def dec(func):
#     def wrapper(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         time1 = time.time()
#         for i in range (100):
#             func(arg1, arg2)
#         time2 = time.time() - time1
#         print('execution time = ', time2)
#     return wrapper
#
# @dec
# def func(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
# func("Vasya", "Pupkin")

# def simple_decorator(*args):
#     def dec(func):
#         def wrapper():
#             print(args)
#             time1 = time.time()
#             for i in range (100):
#                 func()
#             time2 = time.time() - time1
#             print('execution time = ', time2)
#         return wrapper
#
# @simple_decorator("a","b")
# def func():
#     print("Меня зовут")
#     return False
#
# func()


def simple_decorator(*args):
    def actual_simple_decorator(func):
        def wrapper():
            print(args)
            time1 = time.time()
            for i in range (100):
                result = func()
            time2 = time.time() - time1
            print('execution time = ', time2)
            return result
        return wrapper
    return actual_simple_decorator
@simple_decorator('a','b')
def hi():
    print("hi")
    return False

a = hi()