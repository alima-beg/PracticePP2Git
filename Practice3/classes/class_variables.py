
class MyClass:
    x = 42

obj1 = MyClass()
obj2 = MyClass()
print(obj1.x, obj2.x)



class Counter:
    count = 0

Counter.count += 5
print("Текущее значение:", Counter.count)



class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Kanat", 20)
print(p.name, p.age, p.species)



class Circle:
    pi = 3.14159

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.pi * (self.r ** 2)

c = Circle(3)
print("Площадь круга:", c.area())



class Group:
    members = []

Group.members.append("Dias")
Group.members.append("Aruzhan")
Group.members.append("Miras")
print("Список участников:", Group.members)