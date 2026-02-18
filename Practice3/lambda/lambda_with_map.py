numbers = [1, 2, 3, 4, 5]
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings)


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)


numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


numbers = [1, 2, 3, 4, 5]
plus_hundred = list(map(lambda x: x + 100, numbers))
print(plus_hundred)


numbers = [1, 2, 3, 4, 5]
indexed = list(map(lambda x: numbers.index(x) * x, numbers))
print(indexed)