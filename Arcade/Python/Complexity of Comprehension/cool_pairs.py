def coolPairs(a, b):
    # This way we are declaring a SET given an iterable
    # This case, the iterable contains some sum results
    # and some of these sums are equal, when applying
    # the SET function, we get the unique values.
    uniqueSums = {w + x for w in a for x in b if (w * x) % (w + x) == 0}
    return len(uniqueSums)

a = [4, 5, 6, 7, 8]
b = [8, 9, 10, 11, 12]
print(coolPairs(a, b))