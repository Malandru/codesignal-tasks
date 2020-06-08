def createHistogram(ch, assignments):
    return list(map(lambda x: x * ch, assignments))

ch = '*'
assignments = [12, 12, 14, 3, 12, 15, 14]
print(createHistogram(ch, assignments))