"""def print_kadel(n=1):
    count = 0

    while count < n:
        yield "I am Milan kandel"
        count += 1


print(list(print_kadel()))"""

# Fibonacci
[0, 1, 1, 2, 3, 5, ...]


def fibonacci(n=2):
    fv = 0
    sv = 1

    for _ in range(n):
        yield fv
        fv = sv
        sv = fv + sv


fibonacci_series = list(fibonacci(5))

print(fibonacci_series)

"""def fibonacci(n=1):
    fv, sv = 0, 1
    for _ in range(n):
        yield fv
        fv, sv = sv, fv + sv


print(list(fibonacci(10)))
"""
