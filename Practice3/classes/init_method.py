class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Miras", 21)
print(p.name, p.age)


class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

b = Book("World History", "Smith")
print(b.title, b.author)


class Classroom:
    def __init__(self, students):
        self.students = students

c = Classroom(["Dana", "Serik", "Aruzhan"])
print(c.students)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius

circle = Circle(7)
print("Площадь круга:", circle.area)


class Laptop:
    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year

l = Laptop("Apple", 2000, 2025)
print(l.brand, l.price, l.year)