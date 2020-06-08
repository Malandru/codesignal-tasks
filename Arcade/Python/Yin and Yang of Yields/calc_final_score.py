def calcFinalScore(scores, n):
    gen = map(lambda x: x **2, reversed(sorted(scores)))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res

scores = [4, 2, 4, 5]
n = 3
print(calcFinalScore(scores, n))