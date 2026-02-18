class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

s = Student("Bekzat", "Python")
print(s.name, s.subject)




class Animal:
    def sound(self):
        print("Generic sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof!")

Dog().sound()




class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year

c = Car("Toyota", 2020)
print(c.brand, c.year)