import functools
import math

def compose(functions):
    return functools.reduce(lambda a, f: lambda x: a(f(x)), functions)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)

functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]
x = 3.1415
print(functionsComposition(functions, x))