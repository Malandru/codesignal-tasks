import functools
from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda a, b: a * b /gcd(a,b), denominators)

denominators = [2, 3, 4, 5, 6]
print(leastCommonDenominator(denominators))