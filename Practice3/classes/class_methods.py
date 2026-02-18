class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I am " + self.name)

p = Person("Nurlan")
p.greet()



class Math:
    def cube(self, x):
        return x * x * x

m = Math()
print(m.cube(3))



class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

r = Rectangle(5, 6)
print(r.area())



class Counter:
    def __init__(self):
        self.count = 10

    def decrement(self):
        self.count -= 1

c = Counter()
c.decrement()
print(c.count)



class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self, subject):
        print(f"My name is {self.name}, and I am learning {subject}.")

s = Student("Aruzhan")
s.introduce("Java")
