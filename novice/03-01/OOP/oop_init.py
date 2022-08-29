class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print('Halo, nama w', self.name)

p = Person("Tiyanmoe")
p.say_hi()

# The previous 2 lines can also be written as
# Person('Tiyanmoe).say_hi()