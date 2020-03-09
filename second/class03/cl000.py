
to_square =  lambda x: x**2
to_square(123)
print(to_square(12))

# to_square =  lambda x, y: (x**2, y**2)
# print(to_square(12,12))

list1 = [1,2,3,4]
lis2 = [5,6,7,8]
result = map(to_square,list1 )

print(tuple(result))

to_square =  lambda x, y: (x**2, y**2)
list1 = [1,2,3,4]
list2 = [5,6,7,8]
result = map(to_square,list1, list2 )

print(tuple(result))

# find_even = lambda x: not x % 2

# result = filter(lambda x: not x % 2, list1)
# print(result)

# print(find_even(10))

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
#
# r = zip(a,b,c)
# print(list(r))

def func_a(a):
    def func_b(b):
        def func_c(c):
            def func_d(d):
                print(a,b,c,d)
            return func_d
        return func_c
    return func_b
result = func_a(1)(2)(3)(4)

# def decorator(func_to_decorate):
#     def wrapper()
#         result = func_to_decorate()
#         file = open('logs.txt', 'w')
#         file.write(result)
#         file.close
#         return result
#     return wrapper
#
# def func_test():
#     return 'Testing'
#
# r = decorator(func_test)()
# print(r)



# def decorator(func_to_decorate):
#     def wrapper(*args):
#         result = func_to_decorate(*args)
#         file = open('logs.txt', 'w')
#         file.write(result)
#         file.close
#         return result, 12
#     return wrapper
#
# @decorator
# def func_test(string_to_test, second_string_to_test):
#     return string_to_test + second_string_to_test
#
# r = func_test('xzxzx','zxzxc')
# print(r)

def decorator(write_to_file):
    def actual_decorator(func_to_decorate):
        def wrapper(*args):
            result = func_to_decorate(*args)
            if write_to_file:
                file = open('logs.txt', 'w')
                file.write(result)
                file.close
            else:
                print(result)
            return result, 12
        return wrapper
    return actual_decorator

@decorator(write_to_file = True)
def func_test(string_to_test, second_string_to_test):
    return string_to_test + second_string_to_test

r = func_test('xzxzx','zxzxc')
print(r)