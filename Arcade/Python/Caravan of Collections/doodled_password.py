from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda iq: iq[1].rotate(-iq[0]), enumerate(res)), 0)
    return [list(d) for d in res]

digits = [1, 2, 3, 4, 5]
print(doodledPassword(digits))
