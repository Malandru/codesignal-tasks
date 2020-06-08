def multiplicationTable(n):
    return [[x * m for x in range(1, n + 1)] for m in range(1, n + 1)]

print(multiplicationTable(5))