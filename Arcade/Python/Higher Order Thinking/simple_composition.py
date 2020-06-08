import math

def compose(f, g):
    return lambda x: f(g(x))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)

f = "math.log10"
g = "abs"
x = -100
print(simpleComposition(f, g, x))