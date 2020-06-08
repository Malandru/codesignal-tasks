import functools

def primesSum(a, b):
    return functools.reduce(lambda ps, n: ps + n, filter(isprime, range(a, b + 1)), 0)

def isprime(n):
    x = n if n < 100 else int(n ** 0.5)
    for i in range(2, x):
        if n % i == 0: return False
    return n > 1

a = 1
b = 10 ** 5
print(primesSum(a, b))