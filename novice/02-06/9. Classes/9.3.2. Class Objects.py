# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'halodek'

# x = MyClass()
# def __init__(self):
#     self.data = []

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter