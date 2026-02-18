class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()




class X:
    x = 10

class Y:
    y = 20

class Z(X, Y):
    pass

z = Z()
print(z.x, z.y)




class Parent1:
    def __init__(self):
        print("Parent1 init")

class Parent2:
    def __init__(self):
        print("Parent2 init")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child init")

Child()




class Base1:
    def greet(self):
        print("Hello from Base1")

class Base2:
    def greet(self):
        print("Hello from Base2")

class Derived(Base1, Base2):
    def greet(self):
        super().greet()
        print("Hello from Derived")

Derived().greet()