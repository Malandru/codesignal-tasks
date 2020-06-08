from itertools import cycle

def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)


name = "nicecoder"
n = 15
print(cyclicName(name, n))