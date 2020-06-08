def twinsScore(b, m):
    return list(map(lambda w, x: w + x, b, m))

b = [22, 13, 45, 32]
m = [28, 41, 13, 32]
print(twinsScore(b, m))