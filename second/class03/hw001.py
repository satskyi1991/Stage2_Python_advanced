#
#
# myStack = []
# myStack.append(1)
# myStack.append(2)
# myStack.append(3)
#
# print(myStack)
#
# myStack.pop()
# myStack.pop()
# myStack.pop()
#
# print(myStack)
#
#
# from collections import deque
# q = deque()
#
# q.append(1)
# q.append(2)
# q.append(3)
#
# print(q)
# # deque(['eat', 'sleep', 'code'])
#
# print(q.popleft()) # 'eat'
# print(q.popleft()) # 'sleep'
# print(q.popleft()) # 'code'

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()

# s=Stack()
# s.push(4)
# s.push('dog')
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.pop())

class Complex:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    # def __add__(self, other):
    #     self._real = self._real + other._real
    #     self._imag = self._imag + other._imag

    def set(self, real, imag):
        self._real = real
        self._imag = imag

    def get(self):
        return self._real, self._imag

    def add(self, c1, c2):
        real = c1._real + c2._real
        imag = c1._imag + c2._imag
        return Complex(real, imag)

    def sub(self, c1, c2):
        real = c1._real - c2._real
        imag = c1._imag - c2._imag
        return Complex(real, imag)


    def mul(self, c1, c2):
        real = c1._real * c2._real - c1._imag * c2._imag
        imag = c1._imag * c2._real + c1._real * c2._imag
        return Complex(real, imag)

    def abs(self, c):
        return (c._real ** 2 + c._imag ** 2) ** 0.5

comp1 = Complex(1,2)
comp2 = Complex(0,0)
comp3 = Complex(0,0)
comp4 = Complex(0,0)
comp5 = Complex(0,0)

comp2 = comp1.add(Complex(1, 2), Complex(3, 4))
print(comp2.get())
comp3 = comp1.sub(Complex(1, 2), Complex(3, 4))
print(comp3.get())
comp4 = comp1.mul(Complex(1, 2), Complex(3, 4))
print(comp4.get())

comp5 = comp1.abs(Complex(3, 4))
print(comp5.get())
