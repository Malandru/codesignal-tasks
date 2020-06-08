def isInfiniteProcess(a, b):
    return a > b or (b - a) % 2 == 1
    # while not a == b and a <= 20:
    #     a += 1
    #     b -= 1
    # return a > 20


a = 2
b = 6
print(isInfiniteProcess(a,b))
