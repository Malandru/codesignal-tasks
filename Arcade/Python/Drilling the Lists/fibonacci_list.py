import functools

def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda a, x: a + [a[-2] + a[-1]], range(n - 2), [0, 1])]

n = 6
print(fibonacciList(n))