def square(x):
    return x * x


def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

def format_name(first, last):
    return f"{last}, {first}"


def is_even(n):
    return n % 2 == 0


def multiples(n, count):
    return [n * i for i in range(1, count + 1)]