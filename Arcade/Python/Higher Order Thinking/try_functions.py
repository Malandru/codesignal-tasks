import math

def tryFunctions(x, functions):
    return [eval(f)(x) for f in functions]

x = 1
functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]
print(tryFunctions(x, functions))