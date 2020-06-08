def groupDating(male, female):
    return [[], []] if male == female else list(zip(*[(m, f) for m, f in zip(male, female) if m != f]))

male = [5, 28, 14, 99, 17]
female = [5, 14, 28, 99, 16]
print(groupDating(male, female))