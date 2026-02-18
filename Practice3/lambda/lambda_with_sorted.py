students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


numbers = [1, 2, 3, 4, 5]
sorted_by_square = sorted(numbers, key=lambda x: x**2)
print(sorted_by_square)


nums = [-10, 5, -3, 2, -1]
sorted_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_abs)


nums = [-10, 5, -3, 2, -1]
sorted_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_abs)