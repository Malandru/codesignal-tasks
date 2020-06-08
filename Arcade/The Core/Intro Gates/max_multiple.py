def maxMultiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    return maxMultiple(divisor, bound - 1)


divisor = 3
bound = 10
print(maxMultiple(divisor, bound))