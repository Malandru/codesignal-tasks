def correctLineup(athletes):
    return [a for t in zip(athletes[1::2], athletes[::2]) for a in t]
    # return [athletes[i+(-1)**i] for i in range(len(athletes))]
    # return [athletes[i^1] for i in range(len(athletes))]

athletes = [1, 2, 3, 4, 5, 6]
print(correctLineup(athletes))
