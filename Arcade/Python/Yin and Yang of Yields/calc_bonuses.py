def calcBonuses(bonuses, n):
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res

bonuses = [4, 2, 4, 5]
n = 3
print(calcBonuses(bonuses, n))