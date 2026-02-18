numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)


numbers = [5, 10, 15, 20]
plus_ten = list(map(lambda x: x + 10, numbers))
print(plus_ten)


words = ["apple", "banana", "avocado", "grape"]
a_words = list(filter(lambda x: x.startswith("a"), words))
print(a_words)