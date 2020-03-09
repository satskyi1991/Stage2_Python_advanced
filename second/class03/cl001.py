
import time

# from functools import wraps
# def dec1(func):
#
#     @wraps(func)
#     def wrapper(*args):
#         time1 = time.time()
#         for i in range (100):
#             func()
#         time2 = time.time()
#         print(time2-time1)
#     return wrapper
#
# #@dec
# @dec1
# def hello_world():
#     print("hello world")

# from functools import wraps
# def dec1(func):
#
#     @wraps(func)
#     def wrapper(*args):
#         print('*****************')
#         func()
#         print('*****************')
#     return wrapper
#
# #@dec
# @dec1
# def hello_world():
#     print("hello world")
#
# print(hello_world.__wrapped__)

# from functools import wraps
# def dec(func):
#     def wrapper(*args):
#         print('__________________')
#         func()
#         print('__________________')
#     return wrapper
# @dec
# def hello_world():
#     print("hello world")
#
#
# print("hello world")

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_full_name("Vasya", "Pupkin")