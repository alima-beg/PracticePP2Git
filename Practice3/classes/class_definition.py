class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)



class MyClass:
    y = 10

obj = MyClass()
print(obj.y)



class Car:
    brand = "Honda"
    year = 2022

c = Car()
print(c.brand, c.year)



class EmptyBlueprint:
    pass

eb = EmptyBlueprint()
print(type(eb))



class Team:
    members = ["Aliya", "Nurlan", "Serik"]

t = Team()
print(t.members)