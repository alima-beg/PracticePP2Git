
class Animal:
    def sound(self):
        print("Generic sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

Cat().sound()



class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

print(Square(4).area())



class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hello, I am a student")

Student().greet()



class Vehicle:
    def speed(self):
        return 50

class Car(Vehicle):
    def speed(self):
        return 100

print(Car().speed())