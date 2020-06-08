import functools

def mathPractice(numbers):
    return functools.reduce(lambda a, x: a * x[1] if (-1) ** x[0] == 1 else a + x[1], enumerate(numbers), 1)

numbers = [9, 19, 2, 2, 7, 3, 0, 0, 6, 11, 14, 18, 11, 7, 9, 6, 8, 4, 13, 11]
print(mathPractice(numbers))