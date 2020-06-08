import functools

def prefSum(a):
    return functools.reduce(lambda r, x: r + [r[-1] + x], a, [0])[1:]

a = [1, 2, 3]
print(prefSum(a))